import copy

from Phases import *
from Databases import Comp
from ErrorHandling import Error, InputError


class Fluid:

    def __init__(self, components=None, composition=None):

        self.total = TotalPhase()
        self.aqueous = AqueousPhase()
        self.liquid = LiquidPhase()
        self.gaseous = GaseousPhase()
        self.mineral = MineralPhase()

        if components is not None and composition is not None:
            self.addComponents(components, composition)

    def addComponent(self, component, composition, update=True):

        # check that all components exist within the database
        if type(component) != Comp:
            message = "\n\nThe component '{}' does not exist in the database\n".format(component)
            raise InputError(message)

        if type(composition) not in [int, float]:
            message = "\n\nThe composition of component '{}' is incorrectly formatted (int or float expected)\n".format(component)
            raise InputError(message)

        comp = component
        mass = composition
        moles = mass / comp.value.Mr
        phase = comp.value.phase

        # add the component to the respective phase
        self.total.add_component(comp, mass, moles, update=update)

        if phase == PhaseType.AQUEOUS:
            self.aqueous.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.AQUEOUS] = self.aqueous

            return

        if phase == PhaseType.LIQUID:
            self.liquid.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.LIQUID] = self.liquid

            return

        if phase == PhaseType.GASEOUS:
            self.gaseous.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.GASEOUS] = self.gaseous

            return

        if phase == PhaseType.MINERAL:
            self.mineral.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.MINERAL] = self.mineral

            return

        raise Error("\n\nThe component's native phase is not recognised")

    def addComponents(self, components, composition):

        if len(components) != len(composition):
            raise InputError("\n\nThe number of components and compositions provided is not the same")

        for i in range(len(components)):

            self.addComponent(components[i], composition[i], update=False)

        # re-calculate the component mass and mole fractions
        self.total.update()
        self.liquid.update()
        self.aqueous.update()
        self.gaseous.update()
        self.mineral.update()

    def promotePhaseToFluid(self, phaseType):

        if type(phaseType) == PhaseType.TOTAL:
            return copy.deepcopy(self)

        phase = self.total.phases[phaseType]
        components = [i for i in phase.components]
        composition = [phase.mass[i] for i in components]

        newFluid = Fluid(components=components, composition=composition)

        newFluid.total.props = copy.deepcopy(phase.props)
        newFluid.total.phases[phaseType].props = copy.deepcopy(phase.props)

        return newFluid

    def promotePhasesToFluid(self, phaseTypes):

        if PhaseType.TOTAL in phaseTypes:
            return copy.deepcopy(self)

        phases = {}
        components = []
        composition = []
        for phaseType in phaseTypes:
            phase = self.total.phases[phaseType]
            phases[phaseType] = phase
            components = components + [i for i in phase.components]
            composition = composition + [phase.mass[i] for i in phase.components]

        newFluid = Fluid(components=components, composition=composition)

        enthalpy = 0
        entropy = 0
        volume = 0
        P = 0
        T = 0
        for phaseType in phaseTypes:
            newFluid.total.phases[phaseType].props = copy.deepcopy(phases[phaseType].props)

            enthalpy += phases[phaseType].props["h"] * phases[phaseType].props["m"]
            entropy += phases[phaseType].props["s"] * phases[phaseType].props["m"]
            volume += phases[phaseType].props["m"] / (phases[phaseType].props["rho"] + 1e-6)

            P = phases[phaseType].props["P"]
            T = phases[phaseType].props["T"]

        total_mass = sum([newFluid.total.mass[i] for i in newFluid.total.mass])
        newFluid.total.props["P"] = P
        newFluid.total.props["T"] = T
        newFluid.total.props["h"] = enthalpy / total_mass
        newFluid.total.props["s"] = entropy / total_mass
        newFluid.total.props["rho"] = total_mass / (volume + 1e-6)
        newFluid.total.props["m"] = total_mass

        return newFluid

    @staticmethod
    def blendFluids(fluid):
        # TODO
        pass

    # TODO something to print the Fluid, underlying phases and properties
