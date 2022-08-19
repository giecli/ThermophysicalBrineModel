from Phases import PhaseType

from enum import Enum


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

    # TODO generate for all CP and Reaktoro Species

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

