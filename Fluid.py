from Phases import *
from Databases import Comp
from ErrorHandling import Error, InputError
from Phases import Phase

import copy
from typing import List, Union, Dict, Tuple, NoReturn, Optional


class Fluid:
    """
    The Fluid class combines all phases (aqueous, gaseous and mineral)

    Attributes
    ----------
    total : Phase
    aqueous : Phase
    liquid : Phase
    gaseous : Phase
    mineral : Phase

    Methods
    -------
    __init__(self, components=None, composition=None)
    __str__(self)
    addComponent(self, component, composition, update=True)
    addComponents(self, components, composition)
    promotePhaseToFluid(self, phaseType)
    promotePhasesToFluid(self, phaseTypes)

    # TODO something to scale the fluid (i.e. based on mass or volume)

    """
    def __init__(self, components: Optional[Union[List[Comp], Comp]] =None, composition: Optional[Union[List[float], float]] =None):
        """
        Initialises a Fluid object from components and composition (optional)

        Parameters
        ----------
        components (opt): Union[List[Comp], Comp]
            the component(s) to be added to the fluid
        composition (opt): Union[List[Union[int, float]], Union[int, float]
            the composition of the component(s) to be added to the fluid in kg

        Returns
        -------
        Fluid
            a Fluid object

        """

        self.total = TotalPhase()
        self.aqueous = AqueousPhase()
        self.liquid = LiquidPhase()
        self.gaseous = GaseousPhase()
        self.mineral = MineralPhase()
        self.element = ElementPhase()

        if components is not None and composition is not None:
            self.addComponents(components, composition)

    def addComponent(self, component: Comp, composition: float, update: Optional[bool] =True) -> NoReturn:
        """
        add a component to the Fluid

        Parameters
        ----------
        component : Comp
            the component to be added to the FLuid
        composition : Union[int, float]
            the mass of the component to be added to the Fluid in kg
        update : bool
            flag to trigger the recalculation of mass and mole fractions

        Returns
        -------
        NoReturn

        Raises
        ------
        InputError
            if the component does not exist in the database
            if the composition is not in the correct format
        Error
            if the component's native phase is not recognised

        """

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

        if phase == PhaseType.ELEMENT:
            self.element.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.ELEMENT] = self.element

            return

        # TODO for some reason it fails when I run it as is... pls fix
        raise Error("\n\nThe component's native phase is not recognised. Component:{}".format(component))

    def addComponents(self, components: List[Comp], composition: List[float]) -> NoReturn:
        """
        add components to the Fluid

        Parameters
        ----------
        components : Comp
            the component to be added to the FLuid
        composition : Union[int, float]
            the mass of the component to be added to the Fluid in kg

        Returns
        -------
        NoReturn

        Raises
        ------
        InputError
            if the number of components and composition is inconsistent

        """
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

    def promotePhaseToFluid(self, phaseType: PhaseType):
        """
        create a Fluid object for a given Phase

        Parameters
        ----------
        phaseType : PhaseType
            the phase from which the FLuid should be created

        Returns
        -------
        Fluid
            the new Fluid object

        """

        if type(phaseType) == PhaseType.TOTAL:
            return copy.deepcopy(self)

        phase = self.total.phases[phaseType]
        components = [i for i in phase.components]
        composition = [phase.mass[i] for i in components]

        newFluid = Fluid(components=components, composition=composition)

        newFluid.total.props = copy.deepcopy(phase.props)
        newFluid.total.phases[phaseType].props = copy.deepcopy(phase.props)

        return newFluid

    def promotePhasesToFluid(self, phaseTypes: List[PhaseType]):
        """
        create a Fluid object from given Phases

        Parameters
        ----------
        phaseTypes : List[PhaseType]
            the phases from which the FLuid should be created

        Returns
        -------
        Fluid
            the new Fluid object

        """

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

    def __str__(self) -> str:
        """
        creates the Fluid's string representation, i.e. to allow it to be printed

        Returns
        -------
        str
            the Fluid object's string representation

        """

        total = self.total
        text = "Phase: {}\n\n".format(total.phase.name)

        text += "Components:\n"
        for comp in total.components:
            text += "{}, ".format(comp.name)
        text = text[:-2] + "\n\n"

        text += "Composition: \n{:20}|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}|\n".format("Component", "Mass, kg", "MassFrac, -", "Moles, mol", "MoleFrac, -", "In Phase")
        text += "--------------------+---------------+---------------+---------------+---------------+---------------+\n"
        for i, comp in enumerate(total.components):
            text += "{:20}|{:15.3e}|{:15.3e}|{:15.3e}|{:15.3e}|{:>15}|\n".format(comp.name, total.mass[comp], total.massfrac[i], total.moles[comp], total.molefrac[i], comp.value.phase.name)
        text += "--------------------+---------------+---------------+---------------+---------------+---------------+\n"

        text += "\n"
        if self.total.props_calculated:
            text += "Properties: \n"
            text += "Pressure: {} Pa\n".format(self.total.props["P"])
            text += "Temperature: {} K\n".format(self.total.props["T"])
            text += "{:20}|{:<15}|{:<18}|{:<15}|{:<15}|{:<15}|\n".format("Phase", "Enthalpy, kJ/kg", "Entropy, kJ/kg/K", "Rho, kg/m3", "Volume, m3/kg", "Mass, kg")
            text += "--------------------+-----------------+----------------+---------------+---------------+---------------+\n"
            if self.aqueous.components:
                text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.aqueous.phase.name, self.aqueous.props["h"], self.aqueous.props["s"], self.aqueous.props["rho"], self.aqueous.props["v"], self.aqueous.props["m"])
            if self.gaseous.components:
                text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.gaseous.phase.name, self.gaseous.props["h"], self.gaseous.props["s"], self.gaseous.props["rho"], self.gaseous.props["v"], self.gaseous.props["m"])
            if self.mineral.components:
                text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.mineral.phase.name, self.mineral.props["h"], self.mineral.props["s"], self.mineral.props["rho"], self.mineral.props["v"], self.mineral.props["m"])
            text += "--------------------+-----------------+----------------+---------------+---------------+---------------+\n"
            text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.total.phase.name, self.total.props["h"], self.total.props["s"], self.total.props["rho"], self.total.props["v"], self.total.props["m"])
            text += "--------------------+-----------------+----------------+---------------+---------------+---------------+\n"

            if self.total.props.NotCalculated:
                txt = ""
                mass = 0
                for i in self.total.props.NotCalculated:
                    txt += i.value.name + ", "
                    mass += self.total.mass[i]
                txt = txt[:-2]

                text += "The following had to be excluded: {}\n".format(txt)
                text += "This corresponds to a mass of {:.4e} kg or {:.4e} % of the total".format(mass, 100*mass/self.total.props["m"])

        else:
            text += "Properties not yet calculated"
        return text

    def cullComponents(self, moleLimit=1e-15):
        components = [comp for comp in self.total.components if self.total.moles[comp] > moleLimit]
        composition = [self.total.moles[comp] for comp in components]

        self.reset()

        self.addComponents(components, composition)

    def cullPhase(self, phaseType):
        components = [comp for comp in self.total.components if comp.value.phase != phaseType]
        composition = [self.total.moles[comp] for comp in components]

        self.reset()

        self.addComponents(components, composition)

    def reset(self):

        self.total = TotalPhase()
        self.aqueous = AqueousPhase()
        self.liquid = LiquidPhase()
        self.gaseous = GaseousPhase()
        self.mineral = MineralPhase()
        self.element = ElementPhase()

