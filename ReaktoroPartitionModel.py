from Phases import PhaseType
from Databases import LookUp
from ErrorHandling import Error
from Fluid import Fluid

import reaktoro as rkt
from enum import Enum


def initFromElements(fluid, options):
    elements = ""
    for i in fluid.total.elements:
        elements += i + " "
    elements = elements[:-1]

    gaseous = rkt.GaseousPhase(rkt.speciate(elements))
    gaseous.setActivityModel(options.gaseousActivityModel())

    aqueous = rkt.AqueousPhase(rkt.speciate(elements))
    aqueous.setActivityModel(options.aqueousActivtityModel())
    if options.aqueousCO2ActivityModel.value is not None:
        if "C" in fluid.total.elements and "O" in fluid.total.elements:
            aqueous.setActivityModel(rkt.chain(options.aqueousActivtityModel(),
                                               options.aqueousCO2ActivityModel("CO2")))

    mineral = rkt.MineralPhases(rkt.speciate(elements))
    mineral.setActivityModel(options.mineralActivityModel())

    return gaseous, aqueous, mineral, elements


def initFromSpecies(fluid, options):
    elements = ""
    for i in fluid.total.elements:
        elements += i + " "
    elements = elements[:-1]

    aqueous = rkt.AqueousPhase()
    gaseous = rkt.GaseousPhase()
    mineral = rkt.MineralPhases()

    charge = 0
    aqueous_str = ""
    if fluid.aqueous.components:
        for i in fluid.aqueous.components:
            aqueous_str += i.value.alias["RKT"] + " "
            charge += i.value.charge * fluid.total.moles[i]
        aqueous_str = aqueous_str[:-1]

        if abs(charge) > 1e-6:
            raise Error("\n\nThe aqueous phase is not charge balanced. The excess charge is {:.4e}.\nPlease review the input data\n".format(charge))

        aqueous = rkt.AqueousPhase(aqueous_str)

    gaseous_str = ""
    if fluid.gaseous.components:
        for i in fluid.gaseous.components:
            gaseous_str += i.value.alias["RKT"] + " "
        gaseous_str = gaseous_str[:-1]
        gaseous = rkt.GaseousPhase(gaseous_str)

    mineral_str = ""
    if fluid.mineral.components:
        for i in fluid.mineral.components:
            mineral_str += i.value.alias["RKT"] + " "
        mineral_str = mineral_str[:-1]
        mineral = rkt.MineralPhases(mineral_str)

    return gaseous, aqueous, mineral, elements


class ReaktoroPartitionOptions:

    class Database(Enum):
        SUPCRTBL = "supcrtbl"
        BS = "total horse shite"

    class SpeciesMode(Enum):
        ALL = initFromElements
        SELECTED = initFromSpecies

    class AqueousActivityModels(Enum):
        IDEAL = rkt.ActivityModelIdealAqueous
        DAVIES = rkt.ActivityModelDavies
        DEBYE_HUCKEL = rkt.ActivityModelDebyeHuckel
        DEBYE_HUCKEL_KIELLAND = rkt.ActivityModelDebyeHuckelKielland
        DEBYE_HUCKEL_LIMITINGLAW = rkt.ActivityModelDebyeHuckelLimitingLaw
        DEBYE_HUCKEL_PARAMS = rkt.ActivityModelDebyeHuckelParams
        DEBYE_HUCKEL_PHREEQC = rkt.ActivityModelDebyeHuckelPHREEQC
        DEBYE_HUCKEL_WATEQ4F = rkt.ActivityModelDebyeHuckelWATEQ4F
        HKF = rkt.ActivityModelHKF
        PITZER_HMW = rkt.ActivityModelPitzerHMW

    class AqueousCO2ActivityModels(Enum):
        NONE = None
        DRUMMOND = rkt.ActivityModelDrummond
        DUAN_SUN = rkt.ActivityModelDuanSun
        RUMPF = rkt.ActivityModelRumpf

    class GaseousActivityModels(Enum):
        IDEAL = rkt.ActivityModelIdealGas
        PENG_ROBINSON = rkt.ActivityModelPengRobinson
        REDLICH_KWONG = rkt.ActivityModelRedlichKwong
        SOAVE_REDLICH_KWONG = rkt.ActivityModelSoaveRedlichKwong
        VAN_DER_WAALS = rkt.ActivityModelVanDerWaals

    class MineralActivityModels(Enum):
        IDEAL = rkt.ActivityModelIdealSolution(rkt.StateOfMatter.Solid)
        REDLICH_KISTER = rkt.ActivityModelRedlichKister

    def __init__(self):
        self.database = self.Database.SUPCRTBL
        self.speciesMode = self.SpeciesMode.SELECTED

        self.aqueousActivityModel = self.AqueousActivityModels.IDEAL
        self.aqueousCO2ActivityModel = self.AqueousCO2ActivityModels.NONE
        self.gaseousActivityModel = self.GaseousActivityModels.IDEAL
        self.mineralActivityModel = self.MineralActivityModels.IDEAL

        self.strictSucess = True  # raise an error if solve does not converge

        self.debug = False  # create file of reaktoro results
        self.debugFileName = "ReaktoroResults.txt"


class ReaktoroPartition:

    # TODO a P-H Equilibration would be cool too...

    @staticmethod
    def calc(fluid, P, T, options):
        options = options.Reaktoro

        db = rkt.SupcrtDatabase(options.database.value)

        aqueous, gaseous, mineral, elements = options.speciesMode(fluid, options)

        system = rkt.ChemicalSystem(db, aqueous, gaseous, mineral)

        state = rkt.ChemicalState(system)
        for i in range(len(fluid.total.components)):
            state.set(fluid.total.components[i].value.alias["RKT"], fluid.total.massfrac[i], "kg")

        if options.speciesMode == ReaktoroPartitionOptions.SpeciesMode.ALL:
            # this is a total fudge....
            if "O" in elements:
                state.set("O2(aq)", 1e-15, "kg")
            if "H" in elements:
                state.set("H2(aq)", 1e-15, "kg")

        state.pressure(P, "Pa")
        state.temperature(T, "K")

        res = rkt.equilibrate(state)

        if options.strictSucess:
            assert res.optima.succeeded

        if options.debug:
            state.output(options.debugFileName)

        species = {}
        masses = {}
        for phase in state.system().phases().data():
            if phase.name() == "AqueousPhase":
                key = PhaseType.AQUEOUS
            elif phase.name() == "GaseousPhase":
                key = PhaseType.GASEOUS
            elif phase.name() == "MineralPhase":
                key = PhaseType.MINERAL
            else:
                raise Error("\n\n Invalid phase encountered")

            species[key] = [LookUp().withReaktoroName(i.name()) for i in phase.species().data()]
            masses[key] = [state.speciesMass(i.name())[0] for i in phase.species().data()]

        components = []
        composition = []
        for i in species:
            for j in range(len(species[i])):
                components.append(species[i][j])
                composition.append(masses[i][j])

        # now need to build a new fluid from this
        return Fluid(components=components, composition=composition)