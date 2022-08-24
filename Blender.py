from Fluid import Fluid
from PropertyModel import PhaseProperties

from typing import List, Union, Dict, Tuple, NoReturn, Optional


class Blender:
    """
    The Blender class allows two Fluids to be mixed

    Attributes
    ----------
    None

    Methods
    -------
    blend(fluid1, fluid2, ratio1to2, ratio1to2=1.0)

    """

    @staticmethod
    def blend(fluid1: Fluid, fluid2: Fluid, ratio1to2: Optional[float] = 1.0) -> Fluid:
        """
        Mixes two fluids according to a mass-based mixing ration.

        Parameters
        ----------
        fluid1 : Fluid
            the first Fluid to be mixed
        fluid2 : Fluid
            the second Fluid to be mixed
        ratio1to2 : Union[float, int]
            the ratio of the mass of fluid2 to the mass of fluid1

        Returns
        -------
        Fluid
            a Fluid object containing the mixed fluids

        Raises
        ------
        Nothing
        """

        components1 = [i for i in fluid1.total.components]
        components2 = [i for i in fluid2.total.components]

        components = list(set(components1 + components2))

        diff1 = list(set(components) - set(components1))
        diff2 = list(set(components) - set(components2))

        mass1 = {i:fluid1.total.mass[i] for i in fluid1.total.mass}
        for comp in diff1:
            mass1[comp] = 0
        mass2 = {i:fluid2.total.mass[i] for i in fluid2.total.mass}
        for comp in diff2:
            mass2[comp] = 0

        composition = [0 for i in components]
        for i, comp in enumerate(components):
            composition[i] = mass1[comp] + ratio1to2 * mass2[comp]

        new_fluid = Fluid(components=components, composition=composition)

        if fluid1.total.props_calculated and fluid2.total.props_calculated:
            if fluid1.total.props["P"] == fluid2.total.props["P"] and fluid1.total.props["T"] == fluid2.total.props["T"]:
                props = {"P": fluid1.total.props["P"],
                         "T": fluid1.total.props["T"],
                         "h": (fluid1.total.props["m"] * fluid1.total.props["h"] + ratio1to2 * fluid2.total.props["m"] * fluid2.total.props["h"])/(fluid1.total.props["m"] + ratio1to2 * fluid2.total.props["m"]),
                         "s": (fluid1.total.props["m"] * fluid1.total.props["s"] + ratio1to2 * fluid2.total.props["m"] * fluid2.total.props["s"]) / (fluid1.total.props["m"] + ratio1to2 * fluid2.total.props["m"]),
                         "rho":  (fluid1.total.props["m"] + ratio1to2 * fluid2.total.props["m"]) / ((fluid1.total.props["m"] / (fluid1.total.props["rho"] + 1e-6) )+ (ratio1to2 * fluid2.total.props["m"] / (fluid2.total.props["rho"] + 1e-6))),
                         "m": fluid1.total.props["m"] + ratio1to2 * fluid2.total.props["m"]
                         }
                new_fluid.total.props = PhaseProperties(props)
                new_fluid.total.props_calculated = True

                for phase in new_fluid.total.phases:

                    if phase in fluid1.total.phases and phase in fluid2.total.phases:
                        phase1 = fluid1.total.phases[phase]
                        phase2 = fluid2.total.phases[phase]

                        props = {"P": fluid1.total.props["P"],
                                 "T": fluid1.total.props["T"],
                                 "h": (phase1.props["m"] * phase1.props["h"] + ratio1to2 * phase2.props["m"] * phase2.props["h"]) / (phase1.props["m"] + ratio1to2 * phase2.props["m"]),
                                 "s": (phase1.props["m"] * phase1.props["s"] + ratio1to2 * phase2.props["m"] * phase2.props["s"]) / (phase1.props["m"] + ratio1to2 * phase2.props["m"]),
                                 "rho": (phase1.props["m"] + ratio1to2 * phase2.props["m"]) / ((phase1.props["m"] / (phase1.props["rho"] + 1e-6)) + (ratio1to2 * phase2.props["m"] / (phase2.props["rho"] + 1e-6))),
                                 "m": phase1.props["m"] + ratio1to2 * phase2.props["m"]
                                 }
                    else:
                        if phase in fluid1.total.phases:
                            phase_ = fluid1.total.phases[phase]
                        else:
                            phase_ = fluid2.total.phases[phase]

                        props = {"P": fluid1.total.props["P"],
                                 "T": fluid1.total.props["T"],
                                 "h": phase_.props["h"],
                                 "s": phase_.props["s"],
                                 "rho": phase_.props["rho"],
                                 "m": phase_.props["m"]
                                 }

                    new_fluid.total.phases[phase].props = PhaseProperties(props)
                    new_fluid.total.phases[phase].props_calculated = True

        return new_fluid
