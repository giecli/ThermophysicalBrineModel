from enum import Enum


class PhaseType(Enum):
    LIQUID = "liquid"
    AQUEOUS = "aqueous"
    GASEOUS = "gaseous"
    MINERAL = "mineral"
    TOTAL = "total"
    ELEMENT = "element"
    NONE = "none"


class PhaseProperties:
    """
        The Stream subclass summarises the properties of a given phase

        Attributes
        ----------
        P: int, float
            the phase pressure in MPa
        T: int, float
            the phase temperature in K
        h: int, float
            the phase specific enthalpy in kJ/kg
        s: int, float
            the phase specific entropy in kJ/kg/K
        rho: int, float
            the phase density in kg/m3
        m: int, float
            the total mass of this phase

        Methods
        -------
        __init__(phase_type, props)
        __getitem__(item)
        __str__()

    """

    def __init__(self, props):
        """
        Initialises the Stream object

        Parameters
        ----------
        props: Dict
            dictionary of the fluid properties

        """
        # creates a variable for each of the items in props
        vars = (i for i in props)  # plus plenty more

        # assigns the value to each property
        for i in vars:
            setattr(self, i, props[i])

    def __getitem__(self, item: str):
        """
        Allows the property to be retrieved by either "Stream.xzy" or "Stream["xyz"]

        Parameters
        ----------
        item: str
            the name of the property to return. Valid properties as p, t, h, s, x, rho, phase, fluid for now

        Returns
        -------
        float, int
        """

        item = "" + item
        return getattr(self, item)

    def __str__(self):
        """
        Determines the string representation of Stream objects

        Returns
        -------
        text : str
            text string that encompasses all relevant information about the Fluid object
        """

        text = "P: {:.4e} Pa\tT: {} K\th: {:.4e} kJ/kg\t\ts: {:.4e} kJ/kg/K\trho: {:.4e} kg/m3\tm: {:.4e} kg".format(self.P, self.T, self.h, self.s, self.rho, self.m)

        return text


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

        self.props = PhaseProperties({"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "m": 0})
        self.props_calculated = False

    def __str__(self):
        text = "Phase: {}\n\n".format(self.phase)

        text += "Components:\n"
        for comp in self.components:
            text += "{}, ".format(comp.name)
        text = text[:-2] + "\n\n"

        text += "Composition: \n{:20}|{:<15}|{:<15}|{:<15}|{:<15}|\n".format("Component", "Mass, kg", "MassFrac, -", "Moles, mol", "MoleFrac, -")
        text += "--------------------+---------------+---------------+---------------+---------------+\n"
        for i, comp in enumerate(self.components):
            text += "{:20}|{:15.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(comp.name, self.mass[comp], self.massfrac[i], self.moles[comp], self.molefrac[i])

        text += "\nProperties: " + str(self.props) + "\n"

        return text

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

