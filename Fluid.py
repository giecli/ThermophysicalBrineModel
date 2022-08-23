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
    def blendFluids(fluid1, fluid2):

        # TODO branch this out into a separate object

        components1 = [i for i in fluid1.total.components]
        components2 = [i for i in fluid2.total.components]

        components = list(set(components1+components2))

        overlap = list(set(components1) & set(components2))
        if overlap:

            composition = []
            for comp in components:
                if comp in overlap:
                    composition.append(fluid1.total.mass[comp] + fluid2.total.mass[comp])
                elif comp in components1:
                    composition.append(fluid1.total.mass[comp])
                else:
                    composition.append(fluid2.total.mass[comp])

        else:
            composition1 = [fluid1.total.mass[i] for i in components1]
            composition2 = [fluid2.total.mass[i] for i in components2]

            composition = composition1 + composition2

        return Fluid(components=components, composition=composition)

    def __str__(self):

        total = self.total
        text = "Phase: {}\n\n".format(total.phase.name)

        text += "Components:\n"
        for comp in total.components:
            text += "{}, ".format(comp.name)
        text = text[:-2] + "\n\n"

        text += "Composition: \n{:20}|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}|\n".format("Component", "Mass, kg", "MassFrac, -", "Moles, mol", "MoleFrac, -", "In Phase")
        text += "--------------------+---------------+---------------+---------------+---------------+---------------+\n"
        for i, comp in enumerate(total.components):
            text += "{:20}|{:15.3e}|{:15.3e}|{:15.3e}|{:15.3e}|{:>15}\n".format(comp.name, total.mass[comp], total.massfrac[i], total.moles[comp], total.molefrac[i], comp.value.phase.name)
        text += "--------------------+---------------+---------------+---------------+---------------+---------------+\n"

        text += "\n"
        if self.total.props_calculated:
            text += "Properties: \n{:20}|{:<15}|{:<18}|{:<15}|{:<15}|\n".format("Phase", "Enthalpy, kJ/kg", "Entropy, kJ/kg/K", "Rho, kg/m3", "Mass, kg")
            text += "--------------------+-----------------+----------------+---------------+---------------+\n"
            text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|\n".format(self.aqueous.phase.name, self.aqueous.props["h"], self.aqueous.props["s"], self.aqueous.props["rho"], self.aqueous.props["m"])
            text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|\n".format(self.gaseous.phase.name, self.gaseous.props["h"], self.gaseous.props["s"], self.gaseous.props["rho"], self.gaseous.props["m"])
            text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|\n".format(self.mineral.phase.name, self.mineral.props["h"], self.mineral.props["s"], self.mineral.props["rho"], self.mineral.props["m"])
            text += "--------------------+-----------------+----------------+---------------+---------------+\n"
            text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|\n".format(self.total.phase.name, self.total.props["h"], self.total.props["s"], self.total.props["rho"], self.total.props["m"])
            text += "--------------------+-----------------+----------------+---------------+---------------+\n"
        else:
            text += "Properties not yet calculated"
        return text
