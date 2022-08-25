from Databases import Comp
from Phases import Phase
from Constants import *

from enum import Enum
import os
import thermohubclient
import thermofun as fun
import CoolProp as cp
from typing import List, Union, Dict, Tuple, NoReturn, Optional


class ThermoFunPropertyOptions:
    """
        The ThermoFunPropertyOptions class contains all of the ThermoFun property calculation options

        Classes
        -------
        Database

        Attributes
        ----------
        database: self.Database
            the ThermoFun database to be used
        databaseHomeDir: str
            the home director of the ThermoFun database - relative to the project's home directory
        databaseConfigFile: str
            the name of the ThermoHub configuration file - in the databaseHomeDir directory
        massfracCutOff: float
            the minimum mass fraction for a species to be included in the property calculations

        Methods
        -------
        get_database(self, database)
        __init__(self)

    """

    class Database(Enum):
        """
            Database sub-class contains all the ThermoFun databases that can be used
        """
        AQ17 = "aq17-thermofun.json"
        CEMDATA18 = "cemdata18-thermofun.json"
        HERACLES = "heracles-thermofun.json"
        MINES16 = "mines16-thermofun.json"
        MINES19 = "mines19-thermofun.json"
        PSINAGRA = "psinagra-12-07-thermofun.json"
        SLOP16 = "slop16-thermofun.json"
        SLOP98INORGANIC = "slop98-inorganic-thermofun.json"
        SLOP98ORGANIC = "slop98-organic-thermofun.json"

    def get_database(self, database: str):
        """
            retrieves the database from ThermoHub

            Parameters
            ----------
            database: str
                the ThermoFun database name
        """
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
        """
            initialises the ThermoFunPropertyModelOptions
        """
        self.database = self.Database.SLOP98INORGANIC
        self.databaseHomeDir = "ThermoFun"
        self.databaseConfigFile = "hub-connection-config.json"

        self.massfracCutOff = 1e-6


class ThermoFunProperties:
    """
        The ThermoFunProperties class orchestrates the property calculations using ThermoFun

        Methods
        -------
        calc(phase, P, T, options)
    """

    @staticmethod
    def calc(phase: Phase, P: float, T: float, options: ThermoFunPropertyOptions) -> Dict:
        """
            calculates the thermophysical properties of the phase at the specified temperature and pressure

            Parameters
            ----------
            phase: Phase
                the phase to be evaluated
            P: float
                the pressure in Pa
            T: float
                the temperature in K
            options: ThermoFunPropertyOptions
                the calculation options to be used

            Returns
            -------
            props: Dict

            Raises:
            Nothing
        """

        # options = options.ThermoFun

        database = options.databaseHomeDir + "/" + options.database.value
        engine = fun.ThermoEngine(database)

        props = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "m": 0}

        enthalpy = 0
        entropy = 0
        volume = 0
        comp_not_calculated = []
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
                try:
                    properties = engine.thermoPropertiesSubstance(T, P, comp.value.alias["RKT"])
                    properties0 = engine.thermoPropertiesSubstance(Tref, Pref, comp.value.alias["RKT"])

                    enthalpy += phase.mass[comp] * (properties.enthalpy.val - properties0.enthalpy.val) / 1e3
                    entropy += phase.mass[comp] * (properties.entropy.val - properties0.entropy.val) / 1e3
                    if properties.volume.val > 0:
                        volume += properties.volume.val * phase.mass[comp]
                except RuntimeError:
                    # TODO - this is not particularly neat... I should compute their properties somehow... Usually (aq) species
                    comp_not_calculated.append(comp)

        total_mass = sum([phase.mass[i] for i in phase.mass])

        props["P"] = P
        props["T"] = T
        props["h"] = enthalpy / (total_mass + 1e-6)
        props["s"] = entropy / (total_mass + 1e-6)
        props["rho"] = total_mass / (volume + 1e-6)
        props["v"] = volume / total_mass
        props["m"] = total_mass
        props["NotCalculated"] = comp_not_calculated

        return props

