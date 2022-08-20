from Phases import PhaseType
from Components import Databases
from ErrorHandling import Error
from Fluid import Fluid

import reaktoro as rkt


class ReaktoroPartitionOptions:

    pass


class ReaktoroPartition:

    # TODO Need to make it so that the user can set up the Reaktoro calculation
    # themselves (i.e. enabling specific activity models etc.)

    @staticmethod
    def calc(fluid, P, T, options):

        # TODO something to consider the selected Reaktoro options

        db = rkt.SupcrtDatabase('supcrtbl')

        elements = ""
        for i in fluid.total.elements:
            elements += i + " "
        elements = elements[:-1]

        gaseous = rkt.GaseousPhase(rkt.speciate(elements))
        aqueous = rkt.AqueousPhase(rkt.speciate(elements))
        mineral = rkt.MineralPhases(rkt.speciate(elements))

        system = rkt.ChemicalSystem(db, aqueous, gaseous, mineral)

        state = rkt.ChemicalState(system)
        for i in range(len(fluid.total.components)):
            state.set(fluid.total.components[i].value.alias["RKT"], fluid.total.massfrac[i], "kg")

        state.pressure(P, "Pa")
        state.temperature(T, "K")

        res = rkt.equilibrate(state)

        # state.output("test.txt")

        props = rkt.ChemicalProps(state)
        # need to extract some properties I guess

        species = {}
        masses = {}
        for phase in state.system().phases().data():
            if phase.name() == "AqueousPhase":
                key = PhaseType.AQUEOUS
            elif phase.name() == "GaseousPhase":
                key = PhaseType.GASEOUS
            elif phase.name() == "MineralPhase":
                key = PhaseType.MINERAL
            else:
                raise Error("\n\n Invalid phase encountered")

            species[key] = [Databases().withReaktoroName(i.name()) for i in phase.species().data()]
            masses[key] = [state.speciesMass(i.name())[0] for i in phase.species().data()]

        components = []
        composition = []
        for i in species:
            for j in range(len(species[i])):
                components.append(species[i][j])
                composition.append(masses[i][j])

        # now need to build a new fluid from this
        return Fluid(components=components, composition=composition)

