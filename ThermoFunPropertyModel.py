from Databases import Comp
from Constants import *

from enum import Enum
import os
import thermohubclient
import thermofun as fun
import CoolProp as cp


class ThermoFunPropertyOptions:
    #TODO
    pass


class ThermoFunUtils:

    class Databases(Enum):
        AQ17 = "aq17-thermofun.json"
        CEMDATA18 = "cemdata18-thermofun.json"
        HERACLES = "heracles-thermofun.json"
        MINES16 = "mines16-thermofun.json"
        MINES19 = "mines19-thermofun.json"
        PSINAGRA = "psinagra-12-07-thermofun.json"
        SLOP16 = "slop16-thermofun.json"
        SLOP98INORGANIC = "slop98-inorganic-thermofun.json"
        SLOP98ORGANIC = "slop98-organic-thermofun.json"

    home_dir = "ThermoFun"
    config_file = "hub-connection-config.json"

    def get_database(self, database):
        # get the home directory
        home = os.getcwd()

        # navigate to the ThermoFun directory
        ThermoFun_dir = home + "/" + self.home_dir
        os.chdir(ThermoFun_dir)

        # save the ThermoFun database
        dbc = thermohubclient.DatabaseClient(self.config_file)
        dbc.saveDatabase(database.value)

        # navigate back to the home directory
        os.chdir(home)


class ThermoFunProperties:

    # TODO need to improve the way the user selects the database

    @staticmethod
    def calc(phase, P, T, options):

        database_name = ThermoFunUtils.Databases.SLOP98INORGANIC

        database = ThermoFunUtils.home_dir + "/" + database_name.value
        engine = fun.ThermoEngine(database)

        props = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "m": 0}

        enthalpy = 0
        entropy = 0
        volume = 0
        for i in range(len(phase.components)):

            comp = phase.components[i]

            if comp == Comp.WATER:
                calc = cp.AbstractState("?", comp.value.alias["CP"])

                calc.update(cp.PT_INPUTS, Pref, Tref)
                h0 = calc.hmass()
                s0 = calc.smass()

                calc.update(cp.PT_INPUTS, P, T)

                enthalpy += phase.mass[comp] * (calc.hmass() - h0) / 1e3
                entropy += phase.mass[comp] * (calc.smass() - s0) / 1e3
                volume += phase.mass[comp] / calc.rhomass()

            elif phase.massfrac[i] > 1e-6:
                properties = engine.thermoPropertiesSubstance(T, P, comp.value.alias["RKT"])
                properties0 = engine.thermoPropertiesSubstance(Tref, Pref, comp.value.alias["RKT"])

                enthalpy += phase.mass[comp] * (properties.enthalpy.val - properties0.enthalpy.val) / 1e3
                entropy += phase.mass[comp] * (properties.entropy.val - properties0.entropy.val) / 1e3
                if properties.volume.val > 0:
                    volume += properties.volume.val * phase.mass[comp]

        total_mass = sum([phase.mass[i] for i in phase.mass])

        props["P"] = P
        props["T"] = T
        props["h"] = enthalpy/total_mass
        props["s"] = entropy/total_mass
        props["rho"] = total_mass / (volume + 1e-6)
        props["m"] = total_mass

        return props

