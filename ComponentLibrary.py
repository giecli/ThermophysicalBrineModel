from enum import Enum


class Error(Exception):
    pass


class InputError(Error):

    def __init__(self, message):
        self.message = message


class ConvergenceError(Error):

    def __init__(self, message):
        self.message = message


class PhaseType(Enum):
    LIQUID = "liquid"
    AQUEOUS = "aqueous"
    GASEOUS = "gaseous"
    MINERAL = "mineral"
    TOTAL = "total"
    NONE = "none"


class Phase:

    def __init__(self):
        self.phase = PhaseType.NONE
        self.components = []
        self.elements = {}

        self.mass = {}
        self.moles = {}

        self.massfrac = []
        self.molefrac = []

        self.up_to_date = True

    def add_component(self, comp, mass, moles, update=True):

        if comp in self.components:
            self.mass[comp] += mass
            self.moles[comp] += moles
        else:
            self.components.append(comp)
            self.mass[comp] = mass
            self.moles[comp] = moles

            if len(self.elements) == 0:
                self.elements = {i for i in comp.value.elements}

            self.elements.update(comp.value.elements)

        self.up_to_date = False
        if update:
            self.update()

    def update(self):

        if self.up_to_date:
            return

        total_mass = sum(self.mass.values())
        total_moles = sum(self.moles.values())

        self.massfrac = [self.mass[self.components[i]] / total_mass for i in range(len(self.components))]
        self.molefrac = [self.moles[self.components[i]] / total_moles for i in range(len(self.components))]

        self.up_to_date = True


class LiquidPhase(Phase):

    def __init__(self):
        super().__init__()
        self.phase = PhaseType.LIQUID


class AqueousPhase(Phase):

    def __init__(self):
        super().__init__()
        self.phase = PhaseType.AQUEOUS


class GaseousPhase(Phase):

    def __init__(self):
        super().__init__()
        self.phase = PhaseType.GASEOUS


class MineralPhase(Phase):

    def __init__(self):
        super().__init__()
        self.phase = PhaseType.MINERAL


class TotalPhase(Phase):

    def __init__(self):
        super().__init__()
        self.phase = PhaseType.TOTAL
        self.phases = {}


class Species:

    def __init__(self, rkt_name, cp_name, elements, Mr, charge, phase):
        self.name = rkt_name
        self.alias = {"RKT": rkt_name, "CP": cp_name}
        self.elements = elements
        self.Mr = Mr
        self.charge = charge
        self.phase = phase

    def __str__(self):
        text = "Species Name: {} \n".format(self.name)

        text = text + "Phase: {}\n".format(self.phase.value)

        text = text + "Aliases: \n"
        for alias in self.alias:
            text = text + "\t{}: {}\n".format(alias, self.alias[alias])

        text = text + "Elements:\n"
        for element in self.elements:
            text = text + "\t{}\n".format(element)

        text = text + "Molecular Weight: {} kg/mol\n".format(self.Mr)
        text = text + "Charge: {} \n".format(self.charge)

        return text


class Comp(Enum):

    WATER = Species("H2O", "Water", ["H", "O"], 0.01801528, +0, PhaseType.AQUEOUS)
    Na_plus = Species("Na+", None, ["Na"], 0.02298977, +1, PhaseType.AQUEOUS)
    Cl_minus = Species("Cl-", None, ["Cl"], 0.03545300, -1, PhaseType.AQUEOUS)


class Fluid:

    def __init__(self, components, composition):

        # check that same number of components and compositions have been entered
        if len(components) != len(composition):
            raise InputError("\n\nThe number of components and compositions provided is not the same")

        # check that all components exist within the database
        bad_components = [comp for comp in components if type(comp) != Comp]
        if bad_components:
            message = "\n\nThe following components do not exist in the database:\n"
            for comp in bad_components:
                message = message + "\t{}\n".format(comp)
            message = message + "\nPlease check spelling or add components to the database"

            raise InputError(message)

        # check that all compositions have been entered in the right format
        bad_composition = [components[i] for i in range(len(composition)) if type(composition[i]) not in [int, float]]
        if bad_composition:
            message = "\n\nThe following composition(s) are incorrectly formatted (int or float expected):\n"
            for comp in bad_composition:
                message = message + "\t{}\n".format(comp)
            message = message + "\nPlease check input compositions"

            raise InputError(message)

        # the components and compositions are valid, now add them to the respective phases
        self.total = TotalPhase()
        self.aqueous = AqueousPhase()
        self.liquid = LiquidPhase()
        self.gaseous = GaseousPhase()
        self.mineral = MineralPhase()

        charge = 0
        for i in range(len(components)):
            comp = components[i]
            mass = composition[i]
            moles = mass / comp.value.Mr
            charge += moles * comp.value.charge
            phase = comp.value.phase

            self.total.add_component(comp, mass, moles, update=False)
            if phase == PhaseType.AQUEOUS:
                self.aqueous.add_component(comp, mass, moles, update=False)
            elif phase == PhaseType.LIQUID:
                self.liquid.add_component(comp, mass, moles, update=False)
            elif phase == PhaseType.GASEOUS:
                self.gaseous.add_component(comp, mass, moles, update=False)
            elif phase == PhaseType.MINERAL:
                self.mineral.add_component(comp, mass, moles, update=False)

        self.total.update()
        self.liquid.update()
        self.aqueous.update()
        self.gaseous.update()
        self.mineral.update()

