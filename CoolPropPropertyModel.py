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

        props = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "m": 0}

        components = ""
        mass_fracs = []
        for i in range(len(phase.components)):
            if phase.massfrac[i] > options.massfracCutOff:
                components += phase.components[i].value.alias["CP"] + "&"
                mass_fracs.append(phase.massfrac[i])
        components = components[:-1]

        if components:
            calc = cp.AbstractState("?", components)

            if len(components) > 1:
                # may need something to check that the BIC data exists.

                calc.set_mass_fractions(mass_fracs)

            calc.update(cp.PT_INPUTS, Pref, Tref)
            h0 = calc.hmass()
            s0 = calc.smass()

            calc.update(cp.PT_INPUTS, P, T)
            total_mass = sum([phase.mass[i] for i in phase.mass])

            props["P"] = calc.p()
            props["T"] = calc.T()
            props["h"] = (calc.hmass() - h0) / 1e3
            props["s"] = (calc.smass() - s0) / 1e3
            props["rho"] = calc.rhomass()
            props["m"] = total_mass

        return props

