from enum import Enum
import CoolProp as cp
import reaktoro as rkt
import copy


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

        self.enthalpy = None
        self.entropy = None
        self.volume = None
        self.density = None
        self.props = None

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

        self.enthalpy = None
        self.entropy = None
        self.volume = None
        self.density = None
        self.props = None

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

    STEAM = Species("H2O(g)", "Water", ["H", "O"], 0.01801528, +0, PhaseType.GASEOUS)
    WATER = Species("H2O(aq)", "Water", ["H", "O"], 0.01801528, +0, PhaseType.AQUEOUS)
    Na_plus = Species("Na+", None, ["Na"], 0.02298977, +1, PhaseType.AQUEOUS)
    Cl_minus = Species("Cl-", None, ["Cl"], 0.03545300, -1, PhaseType.AQUEOUS)
    H_plus = Species("H+", None, ["H"], 0.001, +1, PhaseType.AQUEOUS)
    H2_aq = Species("H2(aq)", None, ["H"], 0.002, +0, PhaseType.AQUEOUS)
    HO2_minus = Species("HO2-", None, ["H", "O"], 0.033, -1, PhaseType.AQUEOUS)
    O2_aq = Species("O2(aq)", None, ["O"], 0.032, +0, PhaseType.AQUEOUS)
    OH_minus = Species("OH-", None, ["H", "O"], 0.017, +1, PhaseType.AQUEOUS)
    H2O2_aq = Species("H2O2(aq)", None, ["H", "O"], 0.034, +0, PhaseType.AQUEOUS)
    HYDROGEN = Species("H2(g)", "Hydrogen", ["H"], 0.002, +0, PhaseType.GASEOUS)
    OXYGEN = Species("O2(g)", "Oxygen", ["O"], 0.032, +0, PhaseType.GASEOUS)


class Databases:

    reaktoroToComp = {"H2O(g)": Comp.STEAM,
                      "H2O(aq)": Comp.WATER,
                      "Na+": Comp.Na_plus,
                      "Cl-": Comp.Cl_minus,
                      "H+": Comp.H_plus,
                      "H2(aq)": Comp.H2_aq,
                      "HO2-": Comp.HO2_minus,
                      "O2(aq)": Comp.O2_aq,
                      "OH-": Comp.OH_minus,
                      "H2O2(aq)": Comp.H2O2_aq,
                      "H2(g)": Comp.HYDROGEN,
                      "O2(g)": Comp.OXYGEN}

    coolpropToComp = {"Water": Comp.WATER}

    def withReaktoroName(self, name):
        return self.reaktoroToComp[name]

    def withCoolPropName(self, name):
        return self.coolpropToComp[name]

    def generate(self):

        self.reaktoroToComp = {}
        self.coolpropToComp = {}

        for i in Comp:

            if i.value.alias["RKT"] is not None:
                self.reaktoroToComp[i.value.alias["RKT"]] = i
            if i.value.alias["CP"] is not None:
                self.coolpropToComp[i.value.alias["CP"]] = i

        return self


class PartitionModels(Enum):
    USER_ENTERED = "user_entered"
    REAKTORO = "reaktoro"


class PartitionModel:

    def __new__(cls, fluid, P, T):

        return cls.__call__(cls, fluid, P, T)

    def __call__(cls, fluid, P, T):
        return cls.calc(cls, fluid, P, T)

    def calc(cls, fluid, P, T):
        pass


class UserPartition(PartitionModel):

    def calc(self, fluid, P, T):
        print("User Partition")
        return copy.deepcopy(fluid)


class ReaktoroPartition(PartitionModel):

    # Need to make it so that the user can set up the Reaktoro calculation
    # themselves (i.e. enabling specific activity models etc.)

    def calc(self, fluid, P, T):

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

        state.output("test.txt")

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
        return Fluid(components, composition)


class PropertyModels(Enum):
    THERMOFUN = "thermofun"
    COOLPROP = "coolprop"


class PropertyModel:
    Pref = 101325  # Pa
    Tref = 298  # K

    def __new__(cls, phase, P, T):

        return cls.__call__(cls, phase, P, T)

    def __call__(cls, phase, P, T):
        return cls.calc(cls, phase, P, T)

    def calc(cls, phase, P, T):
        pass


class ThermoFunProperties(PropertyModel):

    def calc(self, phase, P, T):
        print("ThermoFun Properties")


class CoolPropProperties(PropertyModel):

    def calc(self, phase, P, T):

        if len(phase.components) == 1:
            # do a single component calculation
            pass
        else:
            # may need something to check that the BIC data exists.
            components = ""
            mass_fracs = []
            for i in range(len(phase.components)):
                components += phase.components[i] + "&"
                mass_fracs.append(phase.massfrac[i])
            components = components[:-1]

            print(components)

            calc = cp.AbstractState("?", components)
            calc.set_mass_fractions(mass_fracs)

            calc.update(cp.PT_INPUTS, self.Pref, self.Tref)
            h0 = calc.hmass()
            s0 = calc.smass()

            calc.update(cp.PT_INPUTS, P, T)
            props = {"P": calc.P(),
                     "T": calc.T(),
                     "h": (calc.hmass() - h0) / 1e3,
                     "s": (calc.smass() - s0)/ 1e3,
                     "rho": calc.rhomass()
                     }
            return props


class Fluid:

    partition_models = {PartitionModels.USER_ENTERED: UserPartition,
                        PartitionModels.REAKTORO: ReaktoroPartition}

    property_models = {PropertyModels.THERMOFUN: ThermoFunProperties,
                       PropertyModels.COOLPROP: CoolPropProperties}

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
            phase = comp.value.phase

            # add the component to the respective phase
            self.total.add_component(comp, mass, moles, update=False)
            if phase == PhaseType.AQUEOUS:
                self.aqueous.add_component(comp, mass, moles, update=False)
            elif phase == PhaseType.LIQUID:
                self.liquid.add_component(comp, mass, moles, update=False)
            elif phase == PhaseType.GASEOUS:
                self.gaseous.add_component(comp, mass, moles, update=False)
            elif phase == PhaseType.MINERAL:
                self.mineral.add_component(comp, mass, moles, update=False)

            # update the total charge imbalance
            charge += moles * comp.value.charge

        # recalculte the component mass and mole fractions
        self.total.update()
        self.liquid.update()
        self.aqueous.update()
        self.gaseous.update()
        self.mineral.update()

        if abs(charge) > 1e-3:
            raise InputError("\n\nThe fluid is not charge balanced. The charge imbalance is {}".format(charge))

    def partition(self, P, T, model):
        return self.partition_models[model](self, P, T,)

    def properties(self, P, T):

        if len(self.aqueous.components) > 0:
            pass

        if len(self.liquid.components) > 0:
            pass

        if len(self.gaseous.components) > 0:
            self.gaseous.props = self.property_models[PropertyModels.COOLPROP](self.gaseous, P, T)

        if len(self.mineral.components) > 0:
            pass

        return self