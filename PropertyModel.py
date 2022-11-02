from ThermoFunPropertyModel import ThermoFunProperties, ThermoFunPropertyOptions
from CoolPropPropertyModel import CoolPropProperties, CoolPropPropertyOptions
from Fluid import Fluid
from ErrorHandling import Error

from Phases import PhaseProperties

from enum import Enum
from typing import List, Union, Dict, Tuple, NoReturn, Optional


class PropertyModelOptions:
    """
        The PropertyModelOptions class contains the options of all property models

        Attributes
        ----------
        ThermFun: ThermoFunPropertyOptions
            The calculation options for the ThermoFunPropertyModel
        CoolProp: CoolPropPropertyOptions
            The calculation options for the CoolPropPropertyModel
    """

    # initialises the ThermoFun and CoolProp property model options
    ThermoFun = ThermoFunPropertyOptions()
    CoolProp = CoolPropPropertyOptions()


class PropertyModels(Enum):
    """
        The PropertyModel class contains links to all property models

        Attributes
        ----------
        THERMOFUN: ThermoFunProperties
            The link to the ThermoFunPropertyModel
        COOLPROP: CoolPropProperties
            The link to the CoolPropPropertyModel
    """

    # the different property models available
    THERMOFUN = ThermoFunProperties
    COOLPROP = CoolPropProperties


class PropertyModel:
    """
        The PropertyModel class orchestrates all property calculations

        Attributes
        ----------
        options: PropertyModelOptions
            the calculation options to be used for the property calculations

        Methods
        -------
        __init__(self, options=PropertyModelOptions())
        calc(self, fluid, P, T)

    """

    def __init__(self, options: Optional[PropertyModelOptions] = PropertyModelOptions()):
        """
            initialises the PropertyModel with the calculation options

            Parameters
            ----------
            options: Optional[PropertyModelOptions]
                the calculation options to be used for the property calculations
        """

        # set the calculation options
        self.options = options

    def calc(self, fluid: Fluid, P: float, T: float) -> Fluid:
        """
            calculates the thermophysical properties of the input fluid

            Parameters
            ----------
            fluid: Fluid
                the fluid whose thermophysical properties should be evaluated
            P: float
                the pressure in Pa
            T: float
                the temperature in K

            Returns
            --------
            fluid: Fluid
                the calculated fluid
        """



        # trigger the property calculations for the aqueous phase
        if fluid.aqueous.components:
            props = PropertyModels.THERMOFUN.value.calc(fluid.aqueous, P, T, self.options.ThermoFun)
            fluid.aqueous.props = PhaseProperties(props)
            fluid.aqueous.props_calculated = True

        # trigger the property calculations for the gaseous phase
        if fluid.gaseous.components:
            props = PropertyModels.COOLPROP.value.calc(fluid.gaseous, P, T, self.options.CoolProp)
            fluid.gaseous.props = PhaseProperties(props)
            fluid.gaseous.props_calculated = True

        # trigger the property calculations for the mineral phase
        if fluid.mineral.components:
            props = PropertyModels.THERMOFUN.value.calc(fluid.mineral, P, T, self.options.ThermoFun)
            fluid.mineral.props = PhaseProperties(props)
            fluid.mineral.props_calculated = True

        # calculate the properties of the total phase
        # init the total enthalpy, entropy, volume, mass and any components that could not be calculated
        enthalpy = 0
        entropy = 0
        volume = 0.
        mass = 0
        comp_not_calculated = []
        for phase in fluid.total.phases:
            phase = fluid.total.phases[phase]
            enthalpy += phase.props["h"] * phase.props["m"]
            entropy += phase.props["s"] * phase.props["m"]
            volume += phase.props["m"] / (phase.props["rho"] + 1e-6)
            mass += phase.props["m"]

            if phase.props["NotCalculated"]:
                comp_not_calculated = comp_not_calculated + phase.props["NotCalculated"]

        # calculate the total mass
        total_mass = sum([fluid.total.mass[i] for i in fluid.total.mass])

        # check if the total mass from the composition is consistent with the mass of the components in phases
        if (total_mass - mass)/total_mass > 1e-3:
            raise Error("The calculation has lost mass. Current loss: {} %".format(100 * (total_mass - mass)/total_mass))

        # calculate the specific properties
        props = {"P": P,
                 "T": T,
                 "h": enthalpy / total_mass,
                 "s": entropy / total_mass,
                 "rho": total_mass / (volume + 1e-6),
                 "v": volume / total_mass,
                 "m": total_mass,
                 "NotCalculated": comp_not_calculated}

        fluid.total.props = PhaseProperties(props)
        fluid.total.props_calculated = True

        return fluid
