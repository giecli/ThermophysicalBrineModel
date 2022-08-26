from Constants import *
from Phases import Phase

import CoolProp as cp
from typing import List, Union, Dict, Tuple, NoReturn


class CoolPropPropertyOptions:
    """
    The settings governing the calculation of fluid properties from CoolProp.

    Attributes
    ----------
    massfracCutOff : float
        the minimum mass fraction for a component to be considered in the property calculations
    """

    def __init__(self):
        self.massfracCutOff = 1e-6


class CoolPropProperties:
    """
    The CoolPropProperties class handles the calculation of fluid properties using CoolProp.

    Methods
    -------
    calc(phase, P, T, options)
    """

    @staticmethod
    def calc(phase: Phase, P: Union[int, float], T: Union[int, float], options: CoolPropPropertyOptions) -> Dict:
        """
        Calculates the properties of a phase (gaseous) at a given temperature and pressure.

        Parameters
        ----------
        phase : Phase
            the (gaseous) phase storing the composition
        P : Union[int, float]
            the pressure in Pa
        T : Union[float, int]
            the temperature in K

        Returns
        -------
        Dict
            a dictionary of the fluid properties

        Raises
        ------
        Nothing
        """

        props = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "v": 0, "m": 0, "NotCalculated": []}

        components = ""
        mass_fracs = []
        for i in range(len(phase.components)):
            if phase.massfrac[i] > options.massfracCutOff:
                components += phase.components[i].value.alias["CP"] + "&"
                mass_fracs.append(phase.massfrac[i])
        components = components[:-1]
        mass_fracs = [i/sum(mass_fracs)  for i in mass_fracs]

        if components:
            calc = cp.AbstractState("?", components)

            if len(components) > 1:
                # may need something to check that the BIC data exists.

                calc.set_mass_fractions(mass_fracs)

            try:
                calc.update(cp.PT_INPUTS, Pref, Tref)
                h0 = calc.hmass()
                s0 = calc.smass()

                calc.update(cp.PT_INPUTS, P, T)

                enthalpy = (calc.hmass() - h0)
                entropy = (calc.smass() - s0)
                volume = 1 / calc.rhomass()

            except ValueError:
                components = components.split("&")

                enthalpy = 0
                entropy = 0
                volume = 0
                for i, comp in enumerate(components):
                    calc = cp.AbstractState("?", comp)
                    calc.update(cp.PT_INPUTS, Pref, Tref)
                    h0 = calc.hmass()
                    s0 = calc.smass()

                    calc.update(cp.PT_INPUTS, P, T)

                    enthalpy += (calc.hmass() - h0) * mass_fracs[i]
                    entropy += (calc.smass() - s0) * mass_fracs[i]
                    volume += mass_fracs[i] / calc.rhomass()

            total_mass = sum([phase.mass[i] for i in phase.mass])
            props["P"] = calc.p()
            props["T"] = calc.T()
            props["h"] = enthalpy / 1e3
            props["s"] = entropy / 1e3
            props["rho"] = 1 / volume
            props["v"] = volume
            props["m"] = total_mass
            props["NotCalculated"] = None

        return props

