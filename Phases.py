from enum import Enum


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
        self.props = {"P": 0,
                      "T": 0,
                      "h": 0,
                      "s": 0,
                      "rho": 0,
                      "m": 0
                      }

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

        self.massfrac = [self.mass[self.components[i]] / (total_mass + 1e-6) for i in range(len(self.components))]
        self.molefrac = [self.moles[self.components[i]] / (total_moles +1e-6) for i in range(len(self.components))]

        self.enthalpy = None
        self.entropy = None
        self.volume = None
        self.density = None
        self.props = {"P": 0,
                      "T": 0,
                      "h": 0,
                      "s": 0,
                      "rho": 0,
                      "m": 0
                      }

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

