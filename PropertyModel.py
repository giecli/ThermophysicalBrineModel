from ThermoFunPropertyModel import ThermoFunProperties, ThermoFunPropertyOptions
from CoolPropPropertyModel import CoolPropProperties, CoolPropPropertyOptions
from ErrorHandling import Error

from Phases import PhaseProperties

from enum import Enum


class PropertyModelOptions:
    ThermoFun = ThermoFunPropertyOptions()
    CoolProp = CoolPropPropertyOptions()


class PropertyModels(Enum):
    THERMOFUN = ThermoFunProperties
    COOLPROP = CoolPropProperties


class PropertyModel:

    def __init__(self, options=PropertyModelOptions()):
        self.options = options

    def calc(self, fluid, P, T):

        if len(fluid.aqueous.components) > 0:
            props = PropertyModels.THERMOFUN.value.calc(fluid.aqueous, P, T, self.options)
            fluid.aqueous.props = PhaseProperties(props)
            fluid.aqueous.props_calculated = True

        # currently there are is no liquid phase soooo
        # if len(fluid.liquid.components) > 0:
        #     fluid.liquid.props = PropertyModels.COOLPROP.value.calc(fluid.liquid, P, T, self.options)

        if len(fluid.gaseous.components) > 0:
            props = PropertyModels.COOLPROP.value.calc(fluid.gaseous, P, T, self.options)
            fluid.gaseous.props = PhaseProperties(props)
            fluid.gaseous.props_calculated = True

        if len(fluid.mineral.components) > 0:
            props = PropertyModels.THERMOFUN.value.calc(fluid.mineral, P, T, self.options)
            fluid.mineral.props = PhaseProperties(props)
            fluid.mineral.props_calculated = True

        enthalpy = 0
        entropy = 0
        volume = 0.
        mass = 0
        for phase in fluid.total.phases:
            phase = fluid.total.phases[phase]
            enthalpy += phase.props["h"] * phase.props["m"]
            entropy += phase.props["s"] * phase.props["m"]
            volume += phase.props["m"] / (phase.props["rho"] + 1e-6)
            mass += phase.props["m"]

        total_mass = sum([fluid.total.mass[i] for i in fluid.total.mass])
        if (total_mass - mass)/total_mass > 1e-3:
            raise Error("The calculation has lost mass. Current loss: {} %".format(100 * (total_mass - mass)/total_mass))

        props = {"P": P,
                 "T": T,
                 "h": enthalpy / total_mass,
                 "s": entropy / total_mass,
                 "rho": total_mass / (volume + 1e-6),
                 "m": total_mass
                 }
        fluid.total.props = PhaseProperties(props)
        fluid.total.props_calculated = True

        return fluid
