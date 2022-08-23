from Databases import Comp
from Constants import *

from enum import Enum
import os
import thermohubclient
import thermofun as fun
import CoolProp as cp


class ThermoFunPropertyOptions:

    class Database(Enum):
        AQ17 = "aq17-thermofun.json"
        CEMDATA18 = "cemdata18-thermofun.json"
        HERACLES = "heracles-thermofun.json"
        MINES16 = "mines16-thermofun.json"
        MINES19 = "mines19-thermofun.json"
        PSINAGRA = "psinagra-12-07-thermofun.json"
        SLOP16 = "slop16-thermofun.json"
        SLOP98INORGANIC = "slop98-inorganic-thermofun.json"
        SLOP98ORGANIC = "slop98-organic-thermofun.json"

    def get_database(self, database):
        # get the home directory
        home = os.getcwd()

        # navigate to the ThermoFun directory
        ThermoFun_dir = home + "/" + self.databaseHomeDir
        os.chdir(ThermoFun_dir)

        # save the ThermoFun database
        dbc = thermohubclient.DatabaseClient(self.databaseConfigFile)
        dbc.saveDatabase(database.value)

        # navigate back to the home directory
        os.chdir(home)

    def __init__(self):
        self.database = self.Database.SLOP98INORGANIC
        self.databaseHomeDir = "ThermoFun"
        self.databaseConfigFile = "hub-connection-config.json"

        self.massfracCutOff = 1e-6


class ThermoFunProperties:

    @staticmethod
    def calc(phase, P, T, options):

        options = options.ThermoFun

        database = options.databaseHomeDir + "/" + options.database.value
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

            elif phase.massfrac[i] > options.massfracCutOff:
                properties = engine.thermoPropertiesSubstance(T, P, comp.value.alias["RKT"])
                properties0 = engine.thermoPropertiesSubstance(Tref, Pref, comp.value.alias["RKT"])

                enthalpy += phase.mass[comp] * (properties.enthalpy.val - properties0.enthalpy.val) / 1e3
                entropy += phase.mass[comp] * (properties.entropy.val - properties0.entropy.val) / 1e3
                if properties.volume.val > 0:
                    volume += properties.volume.val * phase.mass[comp]

        total_mass = sum([phase.mass[i] for i in phase.mass])

        props["P"] = P
        props["T"] = T
        props["h"] = enthalpy/ (total_mass + 1e-6)
        props["s"] = entropy/ (total_mass + 1e-6)
        props["rho"] = total_mass / (volume + 1e-6)
        props["m"] = total_mass

        return props

