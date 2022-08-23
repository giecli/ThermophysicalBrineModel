from Constants import *

import CoolProp as cp


class CoolPropPropertyOptions:
    #TODO
    pass


class CoolPropProperties:

    @staticmethod
    def calc(phase, P, T, options):

        # check if components are present in significant quantities and create the corresponding
        # composition input for CoolProp

        props = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "m": 0}

        components = ""
        mass_fracs = []
        for i in range(len(phase.components)):
            if phase.massfrac[i] > 1e-6:
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

