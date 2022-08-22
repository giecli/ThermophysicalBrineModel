from Species import Species
from Phases import PhaseType

from enum import Enum


class Comp(Enum):
    # these species exist in both CoolProp and Reaktoro
    STEAM = Species("H2O(g)", "Water", ["H", "O"], 0.01801528, +0, PhaseType.GASEOUS)
    WATER = Species("H2O(aq)", "Water", ["H", "O"], 0.01801528, +0, PhaseType.AQUEOUS)
    HYDROGEN = Species("H2(g)", "Hydrogen", ["H"], 0.002, +0, PhaseType.GASEOUS)
    OXYGEN = Species("O2(g)", "Oxygen", ["O"], 0.032, +0, PhaseType.GASEOUS)
    AMMONIA = Species("NH3", "Ammonia", ["N", "H"], 0.0180385, +0, PhaseType.LIQUID)
    AMMONIA_g = Species("NH3(g)", "Ammonia", ["N", "H"], 0.01703052, +0, PhaseType.GASEOUS)
    CARBONDIOXIDE = Species("CO2(g)", "CarbonDioxide", ["C", "O"], 0.0440096, +0, PhaseType.GASEOUS)
    NITROGEN = Species("N2(g)", "Nitrogen", ["N"], 0.0280134, +0, PhaseType.GASEOUS)
    H2S = Species("H2S(g)", "HydrogenSulfide", ["H", "S"], 0.03408088, +0, PhaseType.GASEOUS)
    HELIUM = Species("He(g)", "Helium", ["He"], 0.004002602, +0, PhaseType.GASEOUS)
    ARGON = Species("Ar(g)", "Argon", ["Ar"], 0.039948, +0, PhaseType.GASEOUS)
    METHANE = Species("CH4(g)", "Methane", ["C", "H"], 0.016042459999999998, +0, PhaseType.GASEOUS)
    O2_g = Species("O2(g)", "Oxygen", ["O"], 0.0319988, +0, PhaseType.GASEOUS)
    CO_g = Species("CO(g)", "CarbonMonoxide", ["C", "O"], 0.028010100000000003, +0, PhaseType.GASEOUS)
    C2H4_g = Species("C2H4(g)", "Ethylene", ["C", "H"], 0.028053159999999997, +0, PhaseType.GASEOUS)
    H2_g = Species("H2(g)", "Hydrogen", ["H"], 0.0020158800000000003, +0, PhaseType.GASEOUS)
    He_g = Species("He(g)", "Helium", ["He"], 0.004002602, +0, PhaseType.GASEOUS)
    SO2_g = Species("SO2(g)", "SulfurDioxide", ["S", "O"], 0.0640638, +0, PhaseType.GASEOUS)
    Kr_g = Species("Kr(g)", "Krypton", ["Kr"], 0.083798, +0, PhaseType.GASEOUS)
    Ne_g = Species("Ne(g)", "Neon", ["Ne"], 0.020179700000000002, +0, PhaseType.GASEOUS)
    Xe_g = Species("Xe(g)", "Xenon", ["Xe"], 0.131293, +0, PhaseType.GASEOUS)

    # reaktoro gaseous species
    Rn_g = Species("Rn(g)", None, ["Rn"], 0.222, +0, PhaseType.GASEOUS)
    S2_g = Species("S2(g)", None, ["S"], 0.06412999999999999, +0, PhaseType.GASEOUS)

    # reaktoro ions
    Ag_CO3_minus = Species("Ag(CO3)-", None, ["Ag", "C", "O"], 0.1678771, -1, PhaseType.AQUEOUS)
    Ag_CO3_2_minus3 = Species("Ag(CO3)2---", None, ["Ag", "C", "O"], 0.227886, -3, PhaseType.AQUEOUS)
    Ag_plus = Species("Ag+", None, ["Ag"], 0.1078682, +1, PhaseType.AQUEOUS)
    Ag_plus2 = Species("Ag++", None, ["Ag"], 0.1078682, +2, PhaseType.AQUEOUS)
    AgCl2_minus = Species("AgCl2-", None, ["Ag", "Cl"], 0.1787742, -1, PhaseType.AQUEOUS)
    AgCl3_minus2 = Species("AgCl3--", None, ["Ag", "Cl"], 0.2142272, -2, PhaseType.AQUEOUS)
    AgCl4_minus3 = Species("AgCl4---", None, ["Ag", "Cl"], 0.24968020000000002, -3, PhaseType.AQUEOUS)
    AgO_minus = Species("AgO-", None, ["Ag", "O"], 0.1238676, -1, PhaseType.AQUEOUS)
    Al_plus3 = Species("Al+++", None, ["Al"], 0.026981538, +3, PhaseType.AQUEOUS)
    AlO_plus = Species("AlO+", None, ["Al", "O"], 0.042980938, +1, PhaseType.AQUEOUS)
    AlOH_plus2 = Species("AlOH++", None, ["Al", "O", "H"], 0.043988878, +2, PhaseType.AQUEOUS)
    AlO2_minus = Species("AlO2-", None, ["Al", "O"], 0.058980338, -1, PhaseType.AQUEOUS)
    Au_plus = Species("Au+", None, ["Au"], 0.19696655000000002, +1, PhaseType.AQUEOUS)
    Au_plus3 = Species("Au+++", None, ["Au"], 0.19696655000000002, +3, PhaseType.AQUEOUS)
    BF4_minus = Species("BF4-", None, ["B", "F"], 0.0868046128, -1, PhaseType.AQUEOUS)
    BO2_minus = Species("BO2-", None, ["B", "O"], 0.0428098, -1, PhaseType.AQUEOUS)
    Ba_HCO3_plus = Species("Ba(HCO3)+", None, ["Ba", "H", "C", "O"], 0.19834384, +1, PhaseType.AQUEOUS)
    Ba_plus2 = Species("Ba++", None, ["Ba"], 0.137327, +2, PhaseType.AQUEOUS)
    BaCl_plus = Species("BaCl+", None, ["Ba", "Cl"], 0.17278, +1, PhaseType.AQUEOUS)
    BaOH_plus = Species("BaOH+", None, ["Ba", "O", "H"], 0.15433434, +1, PhaseType.AQUEOUS)
    Be_plus2 = Species("Be++", None, ["Be"], 0.009012181999999999, +2, PhaseType.AQUEOUS)
    BeOH_plus = Species("BeOH+", None, ["Be", "O", "H"], 0.026019522, +1, PhaseType.AQUEOUS)
    HBeO2_minus = Species("HBeO2-", None, ["H", "Be", "O"], 0.042018922, -1, PhaseType.AQUEOUS)
    BeO2_minus2 = Species("BeO2--", None, ["Be", "O"], 0.041010982, -2, PhaseType.AQUEOUS)
    Br_minus = Species("Br-", None, ["Br"], 0.079904, -1, PhaseType.AQUEOUS)
    Br3_minus = Species("Br3-", None, ["Br"], 0.23971199999999998, -1, PhaseType.AQUEOUS)
    BrO_minus = Species("BrO-", None, ["Br", "O"], 0.0959034, -1, PhaseType.AQUEOUS)
    BrO3_minus = Species("BrO3-", None, ["Br", "O"], 0.1279022, -1, PhaseType.AQUEOUS)
    BrO4_minus = Species("BrO4-", None, ["Br", "O"], 0.1439016, -1, PhaseType.AQUEOUS)
    CaOH_plus = Species("CaOH+", None, ["Ca", "O", "H"], 0.057085340000000005, +1, PhaseType.AQUEOUS)
    Ce_plus4 = Species("Ce++++", None, ["Ce"], 0.14011600000000002, +4, PhaseType.AQUEOUS)
    CN_minus = Species("CN-", None, ["C", "N"], 0.0260174, -1, PhaseType.AQUEOUS)
    CO3_minus2 = Species("CO3--", None, ["C", "O"], 0.0600089, -2, PhaseType.AQUEOUS)
    Ca_HCO3_plus = Species("Ca(HCO3)+", None, ["Ca", "H", "C", "O"], 0.10109484, +1, PhaseType.AQUEOUS)
    Ca_plus2 = Species("Ca++", None, ["Ca"], 0.040078, +2, PhaseType.AQUEOUS)
    CaCl_plus = Species("CaCl+", None, ["Ca", "Cl"], 0.075531, +1, PhaseType.AQUEOUS)
    CaF_plus = Species("CaF+", None, ["Ca", "F"], 0.0590764032, +1, PhaseType.AQUEOUS)
    Cd_plus2 = Species("Cd++", None, ["Cd"], 0.112411, +2, PhaseType.AQUEOUS)
    CdOH_plus = Species("CdOH+", None, ["Cd", "O", "H"], 0.12941834, +1, PhaseType.AQUEOUS)
    HCdO2_minus = Species("HCdO2-", None, ["H", "Cd", "O"], 0.14541774000000002, -1, PhaseType.AQUEOUS)
    CdO2_minus2 = Species("CdO2--", None, ["Cd", "O"], 0.14440979999999998, -2, PhaseType.AQUEOUS)
    Ce_plus2 = Species("Ce++", None, ["Ce"], 0.14011600000000002, +2, PhaseType.AQUEOUS)
    Ce_plus3 = Species("Ce+++", None, ["Ce"], 0.14011600000000002, +3, PhaseType.AQUEOUS)
    Cl_minus = Species("Cl-", None, ["Cl"], 0.035453000000000005, -1, PhaseType.AQUEOUS)
    ClO_minus = Species("ClO-", None, ["Cl", "O"], 0.051452399999999995, -1, PhaseType.AQUEOUS)
    ClO2_minus = Species("ClO2-", None, ["Cl", "O"], 0.0674518, -1, PhaseType.AQUEOUS)
    ClO3_minus = Species("ClO3-", None, ["Cl", "O"], 0.0834512, -1, PhaseType.AQUEOUS)
    ClO4_minus = Species("ClO4-", None, ["Cl", "O"], 0.0994506, -1, PhaseType.AQUEOUS)
    Co_plus2 = Species("Co++", None, ["Co"], 0.0589332, +2, PhaseType.AQUEOUS)
    Co_plus3 = Species("Co+++", None, ["Co"], 0.0589332, +3, PhaseType.AQUEOUS)
    CoOH_plus = Species("CoOH+", None, ["Co", "O", "H"], 0.07594054, +1, PhaseType.AQUEOUS)
    HCoO2_minus = Species("HCoO2-", None, ["H", "Co", "O"], 0.09193994000000001, -1, PhaseType.AQUEOUS)
    CoO2_minus2 = Species("CoO2--", None, ["Co", "O"], 0.090932, -2, PhaseType.AQUEOUS)
    CoOH_plus2 = Species("CoOH++", None, ["Co", "O", "H"], 0.07594054, +2, PhaseType.AQUEOUS)
    Cr2O7_minus2 = Species("Cr2O7--", None, ["Cr", "O"], 0.215988, -2, PhaseType.AQUEOUS)
    CrO4_minus2 = Species("CrO4--", None, ["Cr", "O"], 0.1159937, -2, PhaseType.AQUEOUS)
    Cs_plus = Species("Cs+", None, ["Cs"], 0.13290545, +1, PhaseType.AQUEOUS)
    Cu_plus = Species("Cu+", None, ["Cu"], 0.063546, +1, PhaseType.AQUEOUS)
    Cu_plus2 = Species("Cu++", None, ["Cu"], 0.063546, +2, PhaseType.AQUEOUS)
    CuOH_plus = Species("CuOH+", None, ["Cu", "O", "H"], 0.08055334, +1, PhaseType.AQUEOUS)
    HCuO2_minus = Species("HCuO2-", None, ["H", "Cu", "O"], 0.09655274, -1, PhaseType.AQUEOUS)
    CuO2_minus2 = Species("CuO2--", None, ["Cu", "O"], 0.0955448, -2, PhaseType.AQUEOUS)
    Dy_plus2 = Species("Dy++", None, ["Dy"], 0.1625, +2, PhaseType.AQUEOUS)
    Dy_plus3 = Species("Dy+++", None, ["Dy"], 0.1625, +3, PhaseType.AQUEOUS)
    Dy_plus4 = Species("Dy++++", None, ["Dy"], 0.1625, +4, PhaseType.AQUEOUS)
    Er_plus2 = Species("Er++", None, ["Er"], 0.167259, +2, PhaseType.AQUEOUS)
    Er_plus3 = Species("Er+++", None, ["Er"], 0.167259, +3, PhaseType.AQUEOUS)
    Er_plus4 = Species("Er++++", None, ["Er"], 0.167259, +4, PhaseType.AQUEOUS)
    Eu_plus2 = Species("Eu++", None, ["Eu"], 0.151964, +2, PhaseType.AQUEOUS)
    Eu_plus3 = Species("Eu+++", None, ["Eu"], 0.151964, +3, PhaseType.AQUEOUS)
    Eu_plus4 = Species("Eu++++", None, ["Eu"], 0.151964, +4, PhaseType.AQUEOUS)
    F_minus = Species("F-", None, ["F"], 0.0189984032, -1, PhaseType.AQUEOUS)
    Fe_plus2 = Species("Fe++", None, ["Fe"], 0.055845, +2, PhaseType.AQUEOUS)
    Fe_plus3 = Species("Fe+++", None, ["Fe"], 0.055845, +3, PhaseType.AQUEOUS)
    FeCl_plus = Species("FeCl+", None, ["Fe", "Cl"], 0.091298, +1, PhaseType.AQUEOUS)
    FeOH_plus2 = Species("FeOH++", None, ["Fe", "O", "H"], 0.07285234, +2, PhaseType.AQUEOUS)
    FeOH_plus = Species("FeOH+", None, ["Fe", "O", "H"], 0.07285234, +1, PhaseType.AQUEOUS)
    FeO_plus = Species("FeO+", None, ["Fe", "O"], 0.07184439999999999, +1, PhaseType.AQUEOUS)
    HFe2O_minus = Species("HFeO2-", None, ["H", "Fe", "O"], 0.08885174000000001, -1, PhaseType.AQUEOUS)
    FeO2_minus = Species("FeO2-", None, ["Fe", "O"], 0.0878438, -1, PhaseType.AQUEOUS)
    Ga_plus3 = Species("Ga+++", None, ["Ga"], 0.069723, +3, PhaseType.AQUEOUS)
    GaOH_plus2 = Species("GaOH++", None, ["Ga", "O", "H"], 0.08673034, +2, PhaseType.AQUEOUS)
    GaO_plus = Species("GaO+", None, ["Ga", "O"], 0.08572239999999999, +1, PhaseType.AQUEOUS)
    GaO2_minus = Species("GaO2-", None, ["Ga", "O"], 0.1017218, -1, PhaseType.AQUEOUS)
    Gd_plus2 = Species("Gd++", None, ["Gd"], 0.15725, +2, PhaseType.AQUEOUS)
    Gd_plus3 = Species("Gd+++", None, ["Gd"], 0.15725, +3, PhaseType.AQUEOUS)
    Gd_plus4 = Species("Gd++++", None, ["Gd"], 0.15725, +4, PhaseType.AQUEOUS)
    H_plus = Species("H+", None, ["H"], 0.0010079400000000001, +1, PhaseType.AQUEOUS)
    H2AsO3_minus = Species("H2AsO3-", None, ["H", "As", "O"], 0.12493568000000001, -1, PhaseType.AQUEOUS)
    H2AsO4_minus = Species("H2AsO4-", None, ["H", "As", "O"], 0.14093508, -1, PhaseType.AQUEOUS)
    H2P2O7_minus2 = Species("H2P2O7--", None, ["H", "P", "O"], 0.175959202, -2, PhaseType.AQUEOUS)
    H2PO4_minus = Species("H2PO4-", None, ["H", "P", "O"], 0.096987241, -1, PhaseType.AQUEOUS)
    H2VO4_minus = Species("H2VO4-", None, ["H", "V", "O"], 0.11695498, -1, PhaseType.AQUEOUS)
    H3P2O7_minus = Species("H3P2O7-", None, ["H", "P", "O"], 0.176967142, -1, PhaseType.AQUEOUS)
    HAsO4_minus2 = Species("HAsO4--", None, ["H", "As", "O"], 0.13992714, -2, PhaseType.AQUEOUS)
    HCO3_minus = Species("HCO3-", None, ["H", "C", "O"], 0.06101684, -1, PhaseType.AQUEOUS)
    HCrO4_minus = Species("HCrO4-", None, ["H", "Cr", "O"], 0.11700163999999999, -1, PhaseType.AQUEOUS)
    HF2_minus = Species("HF2-", None, ["H", "F"], 0.039004746400000005, -1, PhaseType.AQUEOUS)
    HO2_minus = Species("HO2-", None, ["H", "O"], 0.03300674, -1, PhaseType.AQUEOUS)
    HPO4_minus2 = Species("HPO4--", None, ["H", "P", "O"], 0.095979301, -2, PhaseType.AQUEOUS)
    HS_minus = Species("HS-", None, ["H", "S"], 0.03307294, -1, PhaseType.AQUEOUS)
    HSO3_minus = Species("HSO3-", None, ["H", "S", "O"], 0.08107114, -1, PhaseType.AQUEOUS)
    HSO4_minus = Species("HSO4-", None, ["H", "S", "O"], 0.09707054, -1, PhaseType.AQUEOUS)
    HSO5_minus = Species("HSO5-", None, ["H", "S", "O"], 0.11306994000000001, -1, PhaseType.AQUEOUS)
    HSe_minus = Species("HSe-", None, ["H", "Se"], 0.07996794, -1, PhaseType.AQUEOUS)
    HSeO3_minus = Species("HSeO3-", None, ["H", "Se", "O"], 0.12796614, -1, PhaseType.AQUEOUS)
    HSeO4_minus = Species("HSeO4-", None, ["H", "Se", "O"], 0.14396554, -1, PhaseType.AQUEOUS)
    HSiO3_minus = Species("HSiO3-", None, ["H", "Si", "O"], 0.07709164, -1, PhaseType.AQUEOUS)
    HVO4_minus2 = Species("HVO4--", None, ["H", "V", "O"], 0.11594704, -2, PhaseType.AQUEOUS)
    Hg_plus2 = Species("Hg++", None, ["Hg"], 0.20059, +2, PhaseType.AQUEOUS)
    HgOH_plus = Species("HgOH+", None, ["Hg", "O", "H"], 0.21759734, +1, PhaseType.AQUEOUS)
    HHgO2_minus = Species("HHgO2-", None, ["H", "Hg", "O"], 0.23359674000000002, -1, PhaseType.AQUEOUS)
    Hg2_plus2 = Species("Hg2++", None, ["Hg"], 0.40118, +2, PhaseType.AQUEOUS)
    Ho_plus2 = Species("Ho++", None, ["Ho"], 0.16493032, +2, PhaseType.AQUEOUS)
    Ho_plus3 = Species("Ho+++", None, ["Ho"], 0.16493032, +3, PhaseType.AQUEOUS)
    Ho_plus4 = Species("Ho++++", None, ["Ho"], 0.16493032, +4, PhaseType.AQUEOUS)
    I_minus = Species("I-", None, ["I"], 0.12690447, -1, PhaseType.AQUEOUS)
    I3_minus = Species("I3-", None, ["I"], 0.38071341000000003, -1, PhaseType.AQUEOUS)
    IO_minus = Species("IO-", None, ["I", "O"], 0.14290387000000002, -1, PhaseType.AQUEOUS)
    IO3_minus = Species("IO3-", None, ["I", "O"], 0.17490267, -1, PhaseType.AQUEOUS)
    IO4_minus = Species("IO4-", None, ["I", "O"], 0.19090207, -1, PhaseType.AQUEOUS)
    In_plus3 = Species("In+++", None, ["In"], 0.114818, +3, PhaseType.AQUEOUS)
    InOH_plus2 = Species("InOH++", None, ["In", "O", "H"], 0.13182534, +2, PhaseType.AQUEOUS)
    InO_plus = Species("InO+", None, ["In", "O"], 0.1308174, +1, PhaseType.AQUEOUS)
    InO2_minus = Species("InO2-", None, ["In", "O"], 0.1468168, -1, PhaseType.AQUEOUS)
    K_plus = Species("K+", None, ["K"], 0.0390983, +1, PhaseType.AQUEOUS)
    KSO4_minus = Species("KSO4-", None, ["K", "S", "O"], 0.1351609, -1, PhaseType.AQUEOUS)
    La_plus3 = Species("La+++", None, ["La"], 0.1389055, +3, PhaseType.AQUEOUS)
    Li_plus = Species("Li+", None, ["Li"], 0.006941, +1, PhaseType.AQUEOUS)
    Lu_plus3 = Species("Lu+++", None, ["Lu"], 0.174967, +3, PhaseType.AQUEOUS)
    Lu_plus4 = Species("Lu++++", None, ["Lu"], 0.174967, +4, PhaseType.AQUEOUS)
    Mg_HCO3_plus = Species("Mg(HCO3)+", None, ["Mg", "H", "C", "O"], 0.08532184, +1, PhaseType.AQUEOUS)
    Mg_plus2 = Species("Mg++", None, ["Mg"], 0.024305, +2, PhaseType.AQUEOUS)
    MgCl_plus = Species("MgCl+", None, ["Mg", "Cl"], 0.059758000000000006, +1, PhaseType.AQUEOUS)
    MgF_plus = Species("MgF+", None, ["Mg", "F"], 0.0433034032, +1, PhaseType.AQUEOUS)
    MgOH_plus = Species("MgOH+", None, ["Mg", "O", "H"], 0.041312339999999996, +1, PhaseType.AQUEOUS)
    Mn_plus2 = Species("Mn++", None, ["Mn"], 0.054938049, +2, PhaseType.AQUEOUS)
    Mn_plus3 = Species("Mn+++", None, ["Mn"], 0.054938049, +3, PhaseType.AQUEOUS)
    MnCl_plus = Species("MnCl+", None, ["Mn", "Cl"], 0.090391049, +1, PhaseType.AQUEOUS)
    MnOH_plus = Species("MnOH+", None, ["Mn", "O", "H"], 0.07194538900000001, +1, PhaseType.AQUEOUS)
    HMnO2_minus = Species("HMnO2-", None, ["H", "Mn", "O"], 0.087944789, -1, PhaseType.AQUEOUS)
    MnO2_minus2 = Species("MnO2--", None, ["Mn", "O"], 0.086936849, -2, PhaseType.AQUEOUS)
    MnO4_minus = Species("MnO4-", None, ["Mn", "O"], 0.118935649, -1, PhaseType.AQUEOUS)
    MnO4_minus2 = Species("MnO4--", None, ["Mn", "O"], 0.118935649, -2, PhaseType.AQUEOUS)
    HMoO4_minus = Species("HMoO4-", None, ["H", "Mo", "O"], 0.16094554, -1, PhaseType.AQUEOUS)
    MoO4_minus2 = Species("MoO4--", None, ["Mo", "O"], 0.1599376, -2, PhaseType.AQUEOUS)
    NH4_plus = Species("NH4+", None, ["N", "H"], 0.01803846, +1, PhaseType.AQUEOUS)
    NO2_minus = Species("NO2-", None, ["N", "O"], 0.0460055, -1, PhaseType.AQUEOUS)
    NO3_minus = Species("NO3-", None, ["N", "O"], 0.0620049, -1, PhaseType.AQUEOUS)
    Na_plus = Species("Na+", None, ["Na"], 0.02298977, +1, PhaseType.AQUEOUS)
    Nd_plus2 = Species("Nd++", None, ["Nd"], 0.14424, +2, PhaseType.AQUEOUS)
    Nd_plus3 = Species("Nd+++", None, ["Nd"], 0.14424, +3, PhaseType.AQUEOUS)
    Nd_plus4 = Species("Nd++++", None, ["Nd"], 0.14424, +4, PhaseType.AQUEOUS)
    Ni_plus2 = Species("Ni++", None, ["Ni"], 0.0586934, +2, PhaseType.AQUEOUS)
    NiCl_plus = Species("NiCl+", None, ["Ni", "Cl"], 0.0941464, +1, PhaseType.AQUEOUS)
    NiOH_plus = Species("NiOH+", None, ["Ni", "O", "H"], 0.07570074, +1, PhaseType.AQUEOUS)
    HNiO2_minus = Species("HNiO2-", None, ["H", "Ni", "O"], 0.09170014, -1, PhaseType.AQUEOUS)
    NiO2_minus2 = Species("NiO2--", None, ["Ni", "O"], 0.0906922, -2, PhaseType.AQUEOUS)
    OH_minus = Species("OH-", None, ["O", "H"], 0.01700734, -1, PhaseType.AQUEOUS)
    PO4_minus3 = Species("PO4---", None, ["P", "O"], 0.094971361, -3, PhaseType.AQUEOUS)
    Pb_plus2 = Species("Pb++", None, ["Pb"], 0.2072, +2, PhaseType.AQUEOUS)
    PbCl_plus = Species("PbCl+", None, ["Pb", "Cl"], 0.24265299999999998, +1, PhaseType.AQUEOUS)
    PbCl3_minus = Species("PbCl3-", None, ["Pb", "Cl"], 0.31355900000000003, -1, PhaseType.AQUEOUS)
    PbCl4_minus2 = Species("PbCl4--", None, ["Pb", "Cl"], 0.349012, -2, PhaseType.AQUEOUS)
    PbOH_plus = Species("PbOH+", None, ["Pb", "O", "H"], 0.22420733999999998, +1, PhaseType.AQUEOUS)
    HPbO2_minus = Species("HPbO2-", None, ["H", "Pb", "O"], 0.24020674, -1, PhaseType.AQUEOUS)
    Pd_OH_plus = Species("PdOH+", None, ["Pd", "O", "H"], 0.12342734, +1, PhaseType.AQUEOUS)
    Pd_SO4_2_minus_plus2 = Species("Pd(SO4)2--", None, ["Pd", "S", "O"], 0.2985452, +2, PhaseType.AQUEOUS)
    Pd_SO4_3_minus4 = Species("Pd(SO4)3----", None, ["Pd", "S", "O"], 0.3946078, -4, PhaseType.AQUEOUS)
    Pd_plus2 = Species("Pd++", None, ["Pd"], 0.10642, +2, PhaseType.AQUEOUS)
    PdCl_plus = Species("PdCl+", None, ["Pd", "Cl"], 0.141873, +1, PhaseType.AQUEOUS)
    PdCl3_minus = Species("PdCl3-", None, ["Pd", "Cl"], 0.212779, -1, PhaseType.AQUEOUS)
    PdCl4_minus2 = Species("PdCl4--", None, ["Pd", "Cl"], 0.248232, -2, PhaseType.AQUEOUS)
    Pr_plus2 = Species("Pr++", None, ["Pr"], 0.14090765, +2, PhaseType.AQUEOUS)
    Pr_plus3 = Species("Pr+++", None, ["Pr"], 0.14090765, +3, PhaseType.AQUEOUS)
    Pr_plus4 = Species("Pr++++", None, ["Pr"], 0.14090765, +4, PhaseType.AQUEOUS)
    Pt_OH_plus = Species("PtOH+", None, ["Pt", "O", "H"], 0.21208534, +1, PhaseType.AQUEOUS)
    Pt_SO4_2_minus2 = Species("Pt(SO4)2--", None, ["Pt", "S", "O"], 0.38720319999999997, -2, PhaseType.AQUEOUS)
    Pt_SO4_3_minus4 = Species("Pt(SO4)3----", None, ["Pt", "S", "O"], 0.4832658, -4, PhaseType.AQUEOUS)
    Pt_plus2 = Species("Pt++", None, ["Pt"], 0.195078, +2, PhaseType.AQUEOUS)
    PtCl_plus = Species("PtCl+", None, ["Pt", "Cl"], 0.230531, +1, PhaseType.AQUEOUS)
    PtCl3_minus = Species("PtCl3-", None, ["Pt", "Cl"], 0.301437, -1, PhaseType.AQUEOUS)
    PtCl4_minus2 = Species("PtCl4--", None, ["Pt", "Cl"], 0.33688999999999997, -2, PhaseType.AQUEOUS)
    Ra_plus2 = Species("Ra++", None, ["Ra"], 0.226, +2, PhaseType.AQUEOUS)
    Rb_plus = Species("Rb+", None, ["Rb"], 0.0854678, +1, PhaseType.AQUEOUS)
    ReO4_minus = Species("ReO4-", None, ["Re", "O"], 0.2502046, -1, PhaseType.AQUEOUS)
    Rh_OH_plus = Species("RhOH+", None, ["Rh", "O", "H"], 0.11991284, +1, PhaseType.AQUEOUS)
    Rh_OH_plus2 = Species("RhOH++", None, ["Rh", "O", "H"], 0.11991284, +2, PhaseType.AQUEOUS)
    Rh_SO4_plus = Species("RhSO4+", None, ["Rh", "S", "O"], 0.19896809999999998, +1, PhaseType.AQUEOUS)
    Rh_SO4_2_minus = Species("Rh(SO4)2-", None, ["Rh", "S", "O"], 0.29503070000000003, -1, PhaseType.AQUEOUS)
    Rh_SO4_2_minus2 = Species("Rh(SO4)2--", None, ["Rh", "S", "O"], 0.29503070000000003, -2, PhaseType.AQUEOUS)
    Rh_SO4_3_minus3 = Species("Rh(SO4)3---", None, ["Rh", "S", "O"], 0.3910933, -3, PhaseType.AQUEOUS)
    Rh_SO4_3_minus4 = Species("Rh(SO4)3----", None, ["Rh", "S", "O"], 0.3910933, -4, PhaseType.AQUEOUS)
    Rh_plus2 = Species("Rh++", None, ["Rh"], 0.1029055, +2, PhaseType.AQUEOUS)
    Rh_plus3 = Species("Rh+++", None, ["Rh"], 0.1029055, +3, PhaseType.AQUEOUS)
    RhCl_plus = Species("RhCl+", None, ["Rh", "Cl"], 0.1383585, +1, PhaseType.AQUEOUS)
    RhCl_plus2 = Species("RhCl++", None, ["Rh", "Cl"], 0.1383585, +2, PhaseType.AQUEOUS)
    RhCl2_plus = Species("RhCl2+", None, ["Rh", "Cl"], 0.1738115, +1, PhaseType.AQUEOUS)
    RhCl3_minus = Species("RhCl3-", None, ["Rh", "Cl"], 0.2092645, -1, PhaseType.AQUEOUS)
    RhCl4_minus = Species("RhCl4-", None, ["Rh", "Cl"], 0.2447175, -1, PhaseType.AQUEOUS)
    RhCl4_minus2 = Species("RhCl4--", None, ["Rh", "Cl"], 0.2447175, -2, PhaseType.AQUEOUS)
    RhO_plus = Species("RhO+", None, ["Rh", "O"], 0.1189049, +1, PhaseType.AQUEOUS)
    Ru_OH_plus = Species("RuOH+", None, ["Ru", "O", "H"], 0.11807734, +1, PhaseType.AQUEOUS)
    Ru_OH_plus2 = Species("RuOH++", None, ["Ru", "O", "H"], 0.11807734, +2, PhaseType.AQUEOUS)
    RuO4_minus2 = Species("RuO4--", None, ["Ru", "O"], 0.1650676, -2, PhaseType.AQUEOUS)
    Ru_SO4_plus = Species("RuSO4+", None, ["Ru", "S", "O"], 0.1971326, +1, PhaseType.AQUEOUS)
    Ru_SO4_2_minus = Species("Ru(SO4)2-", None, ["Ru", "S", "O"], 0.2931952, -1, PhaseType.AQUEOUS)
    Ru_SO4_2_minus2 = Species("Ru(SO4)2--", None, ["Ru", "S", "O"], 0.2931952, -2, PhaseType.AQUEOUS)
    Ru_SO4_3_minus3 = Species("Ru(SO4)3---", None, ["Ru", "S", "O"], 0.3892578, -3, PhaseType.AQUEOUS)
    Ru_SO4_3_minus4 = Species("Ru(SO4)3----", None, ["Ru", "S", "O"], 0.3892578, -4, PhaseType.AQUEOUS)
    Ru_plus2 = Species("Ru++", None, ["Ru"], 0.10107, +2, PhaseType.AQUEOUS)
    Ru_plus3 = Species("Ru+++", None, ["Ru"], 0.10107, +3, PhaseType.AQUEOUS)
    RuCl_plus = Species("RuCl+", None, ["Ru", "Cl"], 0.136523, +1, PhaseType.AQUEOUS)
    RuCl_plus2 = Species("RuCl++", None, ["Ru", "Cl"], 0.136523, +2, PhaseType.AQUEOUS)
    RuCl2_plus = Species("RuCl2+", None, ["Ru", "Cl"], 0.171976, +1, PhaseType.AQUEOUS)
    RuCl3_minus = Species("RuCl3-", None, ["Ru", "Cl"], 0.207429, -1, PhaseType.AQUEOUS)
    RuCl4_minus = Species("RuCl4-", None, ["Ru", "Cl"], 0.24288200000000001, -1, PhaseType.AQUEOUS)
    RuCl4_minus2 = Species("RuCl4--", None, ["Ru", "Cl"], 0.24288200000000001, -2, PhaseType.AQUEOUS)
    Ru_plusCl_5_minus_plus2 = Species("RuCl5--", None, ["Ru", "Cl"], 0.278335, +2, PhaseType.AQUEOUS)
    RuCl6_minus3 = Species("RuCl6---", None, ["Ru", "Cl"], 0.313788, -3, PhaseType.AQUEOUS)
    RuO_plus = Species("RuO+", None, ["Ru", "O"], 0.1170694, +1, PhaseType.AQUEOUS)
    S2_minus2 = Species("S2--", None, ["S"], 0.06412999999999999, -2, PhaseType.AQUEOUS)
    S2O3_minus2 = Species("S2O3--", None, ["S", "O"], 0.11212820000000001, -2, PhaseType.AQUEOUS)
    HS2O3_minus = Species("HS2O3-", None, ["H", "S", "O"], 0.11313614, -1, PhaseType.AQUEOUS)
    S2O4_minus2 = Species("S2O4--", None, ["S", "O"], 0.1281276, -2, PhaseType.AQUEOUS)
    HS2O4_minus = Species("HS2O4-", None, ["H", "S", "O"], 0.12913554, -1, PhaseType.AQUEOUS)
    S2O5_minus2 = Species("S2O5--", None, ["S", "O"], 0.144127, -2, PhaseType.AQUEOUS)
    S2O6_minus2 = Species("S2O6--", None, ["S", "O"], 0.1601264, -2, PhaseType.AQUEOUS)
    S2O8_minus2 = Species("S2O8--", None, ["S", "O"], 0.1921252, -2, PhaseType.AQUEOUS)
    S3_minus2 = Species("S3--", None, ["S"], 0.09619499999999999, -2, PhaseType.AQUEOUS)
    S3O6_minus2 = Species("S3O6--", None, ["S", "O"], 0.19219139999999998, -2, PhaseType.AQUEOUS)
    S4_minus2 = Species("S4--", None, ["S"], 0.12825999999999999, -2, PhaseType.AQUEOUS)
    S4O6_minus2 = Species("S4O6--", None, ["S", "O"], 0.22425640000000002, -2, PhaseType.AQUEOUS)
    S5_minus2 = Species("S5--", None, ["S"], 0.160325, -2, PhaseType.AQUEOUS)
    S5O6_minus2 = Species("S5O6--", None, ["S", "O"], 0.2563214, -2, PhaseType.AQUEOUS)
    SO3_minus2 = Species("SO3--", None, ["S", "O"], 0.0800632, -2, PhaseType.AQUEOUS)
    SO4_minus2 = Species("SO4--", None, ["S", "O"], 0.0960626, -2, PhaseType.AQUEOUS)
    Sc_plus3 = Species("Sc+++", None, ["Sc"], 0.04495591, +3, PhaseType.AQUEOUS)
    ScOH_plus2 = Species("ScOH++", None, ["Sc", "O", "H"], 0.061963250000000004, +2, PhaseType.AQUEOUS)
    ScO_plus = Species("ScO+", None, ["Sc", "O"], 0.06095531, +1, PhaseType.AQUEOUS)
    ScO2_minus = Species("ScO2-", None, ["Sc", "O"], 0.07695471000000001, -1, PhaseType.AQUEOUS)
    SeO3_minus2 = Species("SeO3--", None, ["Se", "O"], 0.1269582, -2, PhaseType.AQUEOUS)
    SeO4_minus2 = Species("SeO4--", None, ["Se", "O"], 0.14295760000000002, -2, PhaseType.AQUEOUS)
    SiF6_minus2 = Species("SiF6--", None, ["Si", "F"], 0.14207591919999998, -2, PhaseType.AQUEOUS)
    Sm_plus2 = Species("Sm++", None, ["Sm"], 0.15036000000000002, +2, PhaseType.AQUEOUS)
    Sm_plus3 = Species("Sm+++", None, ["Sm"], 0.15036000000000002, +3, PhaseType.AQUEOUS)
    Sm_plus4 = Species("Sm++++", None, ["Sm"], 0.15036000000000002, +4, PhaseType.AQUEOUS)
    Sn_plus2 = Species("Sn++", None, ["Sn"], 0.11871, +2, PhaseType.AQUEOUS)
    SnOH_plus = Species("SnOH+", None, ["Sn", "O", "H"], 0.13571734000000002, +1, PhaseType.AQUEOUS)
    HSnO2_minus = Species("HSnO2-", None, ["H", "Sn", "O"], 0.15171674, -1, PhaseType.AQUEOUS)
    Sr_HCO3_plus = Species("Sr(HCO3)+", None, ["Sr", "H", "C", "O"], 0.14863684000000002, +1, PhaseType.AQUEOUS)
    Sr_plus2 = Species("Sr++", None, ["Sr"], 0.08762, +2, PhaseType.AQUEOUS)
    SrCl_plus = Species("SrCl+", None, ["Sr", "Cl"], 0.12307299999999999, +1, PhaseType.AQUEOUS)
    SrF_plus = Species("SrF+", None, ["Sr", "F"], 0.1066184032, +1, PhaseType.AQUEOUS)
    SrOH_plus = Species("SrOH+", None, ["Sr", "O", "H"], 0.10462734, +1, PhaseType.AQUEOUS)
    Tb_plus2 = Species("Tb++", None, ["Tb"], 0.15892534, +2, PhaseType.AQUEOUS)
    Tb_plus3 = Species("Tb+++", None, ["Tb"], 0.15892534, +3, PhaseType.AQUEOUS)
    Tb_plus4 = Species("Tb++++", None, ["Tb"], 0.15892534, +4, PhaseType.AQUEOUS)
    Th_plus4 = Species("Th++++", None, ["Th"], 0.2320381, +4, PhaseType.AQUEOUS)
    Tl_plus = Species("Tl+", None, ["Tl"], 0.2043833, +1, PhaseType.AQUEOUS)
    Tl_plus3 = Species("Tl+++", None, ["Tl"], 0.2043833, +3, PhaseType.AQUEOUS)
    TlOH_plus2 = Species("TlOH++", None, ["Tl", "O", "H"], 0.22139064, +2, PhaseType.AQUEOUS)
    TlO_plus = Species("TlO+", None, ["Tl", "O"], 0.2203827, +1, PhaseType.AQUEOUS)
    TlO2_minus = Species("TlO2-", None, ["Tl", "O"], 0.2363821, -1, PhaseType.AQUEOUS)
    Tm_plus2 = Species("Tm++", None, ["Tm"], 0.16893421, +2, PhaseType.AQUEOUS)
    Tm_plus3 = Species("Tm+++", None, ["Tm"], 0.16893421, +3, PhaseType.AQUEOUS)
    Tm_plus4 = Species("Tm++++", None, ["Tm"], 0.16893421, +4, PhaseType.AQUEOUS)
    U_plus3 = Species("U+++", None, ["U"], 0.23802890999999998, +3, PhaseType.AQUEOUS)
    U_plus4 = Species("U++++", None, ["U"], 0.23802890999999998, +4, PhaseType.AQUEOUS)
    UO2_plus = Species("UO2+", None, ["U", "O"], 0.27002771000000003, +1, PhaseType.AQUEOUS)
    UO2_plus2 = Species("UO2++", None, ["U", "O"], 0.27002771000000003, +2, PhaseType.AQUEOUS)
    VO_plus = Species("VO+", None, ["V", "O"], 0.0669409, +1, PhaseType.AQUEOUS)
    VO_plus2 = Species("VO++", None, ["V", "O"], 0.0669409, +2, PhaseType.AQUEOUS)
    VOH_plus = Species("VOH+", None, ["V", "O", "H"], 0.06794884000000001, +1, PhaseType.AQUEOUS)
    VOH_plus2 = Species("VOH++", None, ["V", "O", "H"], 0.06794884000000001, +2, PhaseType.AQUEOUS)
    VO2_plus = Species("VO2+", None, ["V", "O"], 0.0829403, +1, PhaseType.AQUEOUS)
    VOOH_plus = Species("VOOH+", None, ["V", "O", "H"], 0.08394824, +1, PhaseType.AQUEOUS)
    WO4_minus2 = Species("WO4--", None, ["W", "O"], 0.24783760000000002, -2, PhaseType.AQUEOUS)
    HWO4_minus = Species("HWO4-", None, ["H", "W", "O"], 0.24884554, -1, PhaseType.AQUEOUS)
    Y_plus3 = Species("Y+++", None, ["Y"], 0.08890585, +3, PhaseType.AQUEOUS)
    YOH_plus2 = Species("YOH++", None, ["Y", "O", "H"], 0.10591319, +2, PhaseType.AQUEOUS)
    YO_plus = Species("YO+", None, ["Y", "O"], 0.10490524999999999, +1, PhaseType.AQUEOUS)
    YO2_minus = Species("YO2-", None, ["Y", "O"], 0.12090465, -1, PhaseType.AQUEOUS)
    Yb_plus2 = Species("Yb++", None, ["Yb"], 0.17304, +2, PhaseType.AQUEOUS)
    Yb_plus3 = Species("Yb+++", None, ["Yb"], 0.17304, +3, PhaseType.AQUEOUS)
    Yb_plus4 = Species("Yb++++", None, ["Yb"], 0.17304, +4, PhaseType.AQUEOUS)
    Zn_plus2 = Species("Zn++", None, ["Zn"], 0.06540900000000001, +2, PhaseType.AQUEOUS)
    ZnCl_plus = Species("ZnCl+", None, ["Zn", "Cl"], 0.100862, +1, PhaseType.AQUEOUS)
    ZnCl3_minus = Species("ZnCl3-", None, ["Zn", "Cl"], 0.171768, -1, PhaseType.AQUEOUS)
    ZnOH_plus = Species("ZnOH+", None, ["Zn", "O", "H"], 0.08241634, +1, PhaseType.AQUEOUS)
    HZnO2_minus = Species("HZnO2-", None, ["H", "Zn", "O"], 0.09841574, -1, PhaseType.AQUEOUS)
    ZnO2_minus2 = Species("ZnO2--", None, ["Zn", "O"], 0.09740779999999999, -2, PhaseType.AQUEOUS)
    U_OH_plus2 = Species("UOH++", None, ["U", "O", "H"], 0.25503625, +2, PhaseType.AQUEOUS)
    UO_plus = Species("UO+", None, ["U", "O"], 0.25402831, +1, PhaseType.AQUEOUS)
    U_OH_plus3 = Species("U(OH)+++", None, ["U", "O", "H"], 0.25503625, +3, PhaseType.AQUEOUS)
    UO_plus2 = Species("UO++", None, ["U", "O"], 0.25402831, +2, PhaseType.AQUEOUS)
    HUO2_plus = Species("HUO2+", None, ["U", "O", "H"], 0.27103564999999996, +1, PhaseType.AQUEOUS)
    HUO3_minus = Species("HUO3-", None, ["U", "O", "H"], 0.28703505, -1, PhaseType.AQUEOUS)
    UO3_minus = Species("UO3-", None, ["U", "O"], 0.28602711, -1, PhaseType.AQUEOUS)
    UO2OH_plus = Species("UO2OH+", None, ["U", "O", "H"], 0.28703505, +1, PhaseType.AQUEOUS)
    HUO4_minus = Species("HUO4-", None, ["U", "O", "H"], 0.30303445, -1, PhaseType.AQUEOUS)
    UO4_minus2 = Species("UO4--", None, ["U", "O"], 0.30202650999999997, -2, PhaseType.AQUEOUS)
    Fr_plus = Species("Fr+", None, ["Fr"], 0.223, +1, PhaseType.AQUEOUS)
    OCN_minus = Species("OCN-", None, ["O", "C", "N"], 0.04201680000000001, -1, PhaseType.AQUEOUS)
    SCN_minus = Species("SCN-", None, ["S", "C", "N"], 0.0580824, -1, PhaseType.AQUEOUS)
    SeCN_minus = Species("SeCN-", None, ["Se", "C", "N"], 0.1049774, -1, PhaseType.AQUEOUS)
    HNO2_minus = Species("HN2O2-", None, ["H", "N", "O"], 0.06102014, -1, PhaseType.AQUEOUS)
    N2O2_minus2 = Species("N2O2--", None, ["N", "O"], 0.0600122, -2, PhaseType.AQUEOUS)
    N2H5_plus = Species("N2H5+", None, ["N", "H"], 0.0330531, +1, PhaseType.AQUEOUS)
    N2H6_plus2 = Species("N2H6++", None, ["N", "H"], 0.03406104, +2, PhaseType.AQUEOUS)
    H2PO2_minus = Species("H2PO2-", None, ["H", "P", "O"], 0.064988441, -1, PhaseType.AQUEOUS)
    H2PO3_minus = Species("H2PO3-", None, ["H", "P", "O"], 0.080987841, -1, PhaseType.AQUEOUS)
    HPO3_minus2 = Species("HPO3--", None, ["H", "P", "O"], 0.07997990099999999, -2, PhaseType.AQUEOUS)
    P2O7_minus4 = Species("P2O7----", None, ["P", "O"], 0.17394332199999998, -4, PhaseType.AQUEOUS)
    HP2O7_minus3 = Species("HP2O7---", None, ["H", "P", "O"], 0.17495126200000002, -3, PhaseType.AQUEOUS)
    AsO4_minus3 = Species("AsO4---", None, ["As", "O"], 0.1389192, -3, PhaseType.AQUEOUS)
    AsO2_minus = Species("AsO2-", None, ["As", "O"], 0.1069204, -1, PhaseType.AQUEOUS)
    SbO2_minus = Species("SbO2-", None, ["Sb", "O"], 0.1537588, -1, PhaseType.AQUEOUS)
    Bi_plus3 = Species("Bi+++", None, ["Bi"], 0.20898038, +3, PhaseType.AQUEOUS)
    BiO_plus = Species("BiO+", None, ["Bi", "O"], 0.22497978000000002, +1, PhaseType.AQUEOUS)
    BiOH_plus2 = Species("BiOH++", None, ["Bi", "O", "H"], 0.22598772, +2, PhaseType.AQUEOUS)
    BiO2_minus = Species("BiO2-", None, ["Bi", "O"], 0.24097918000000002, -1, PhaseType.AQUEOUS)
    V_plus2 = Species("V++", None, ["V"], 0.0509415, +2, PhaseType.AQUEOUS)
    V_plus3 = Species("V+++", None, ["V"], 0.0509415, +3, PhaseType.AQUEOUS)
    VO4_minus3 = Species("VO4---", None, ["V", "O"], 0.1149391, -3, PhaseType.AQUEOUS)
    Cr_plus2 = Species("Cr++", None, ["Cr"], 0.051996099999999996, +2, PhaseType.AQUEOUS)
    Cr_plus3 = Species("Cr+++", None, ["Cr"], 0.051996099999999996, +3, PhaseType.AQUEOUS)
    CrOH_plus2 = Species("CrOH++", None, ["Cr", "O", "H"], 0.06900344, +2, PhaseType.AQUEOUS)
    CrO_plus = Species("CrO+", None, ["Cr", "O"], 0.0679955, +1, PhaseType.AQUEOUS)
    CrO2_minus = Species("CrO2-", None, ["Cr", "O"], 0.0839949, -1, PhaseType.AQUEOUS)
    Zr_plus4 = Species("Zr++++", None, ["Zr"], 0.091224, +4, PhaseType.AQUEOUS)
    Zr_OH_plus3 = Species("ZrOH+++", None, ["Zr", "O", "H"], 0.10823134000000001, +3, PhaseType.AQUEOUS)
    ZrO_plus2 = Species("ZrO++", None, ["Zr", "O"], 0.1072234, +2, PhaseType.AQUEOUS)
    HZrO2_plus = Species("HZrO2+", None, ["Zr", "O", "H"], 0.12423073999999999, +1, PhaseType.AQUEOUS)
    HZrO3_minus = Species("HZrO3-", None, ["Zr", "O", "H"], 0.14023014, -1, PhaseType.AQUEOUS)
    NbO3_minus = Species("NbO3-", None, ["Nb", "O"], 0.14090458, -1, PhaseType.AQUEOUS)
    TcO4_minus = Species("TcO4-", None, ["Tc", "O"], 0.16199760000000002, -1, PhaseType.AQUEOUS)
    Pm_plus2 = Species("Pm++", None, ["Pm"], 0.145, +2, PhaseType.AQUEOUS)
    Pm_plus3 = Species("Pm+++", None, ["Pm"], 0.145, +3, PhaseType.AQUEOUS)
    Pm_plus4 = Species("Pm++++", None, ["Pm"], 0.145, +4, PhaseType.AQUEOUS)
    Hf_plus4 = Species("Hf++++", None, ["Hf"], 0.17849, +4, PhaseType.AQUEOUS)
    HfOH_plus3 = Species("HfOH+++", None, ["Hf", "O", "H"], 0.19549734000000002, +3, PhaseType.AQUEOUS)
    HfO_plus2 = Species("HfO++", None, ["Hf", "O"], 0.19448939999999998, +2, PhaseType.AQUEOUS)
    HHfO2_plus = Species("HHfO2+", None, ["H", "Hf", "O"], 0.21149674, +1, PhaseType.AQUEOUS)
    HHfO3_minus = Species("HHfO3-", None, ["H", "Hf", "O"], 0.22749613999999999, -1, PhaseType.AQUEOUS)
    La_plus2 = Species("La++", None, ["La"], 0.1389055, +2, PhaseType.AQUEOUS)
    LaCO3_plus = Species("LaCO3+", None, ["La", "C", "O"], 0.1989144, +1, PhaseType.AQUEOUS)
    LaHCO3_plus2 = Species("LaHCO3++", None, ["La", "H", "C", "O"], 0.19992234, +2, PhaseType.AQUEOUS)
    LaOH_plus2 = Species("LaOH++", None, ["La", "O", "H"], 0.15591284, +2, PhaseType.AQUEOUS)
    LaO_plus = Species("LaO+", None, ["La", "O"], 0.15490489999999998, +1, PhaseType.AQUEOUS)
    LaO2_minus = Species("LaO2-", None, ["La", "O"], 0.1709043, -1, PhaseType.AQUEOUS)
    LaCl_plus2 = Species("LaCl++", None, ["La", "Cl"], 0.1743585, +2, PhaseType.AQUEOUS)
    LaCl2_plus = Species("LaCl2+", None, ["La", "Cl"], 0.20981149999999998, +1, PhaseType.AQUEOUS)
    LaCl4_minus = Species("LaCl4-", None, ["La", "Cl"], 0.28071749999999995, -1, PhaseType.AQUEOUS)
    LaNO3_plus2 = Species("LaNO3++", None, ["La", "N", "O"], 0.20091040000000002, +2, PhaseType.AQUEOUS)
    LaF_plus2 = Species("LaF++", None, ["La", "F"], 0.1579039032, +2, PhaseType.AQUEOUS)
    LaF2_plus = Species("LaF2+", None, ["La", "F"], 0.1769023064, +1, PhaseType.AQUEOUS)
    LaF4_minus = Species("LaF4-", None, ["La", "F"], 0.21489911280000001, -1, PhaseType.AQUEOUS)
    LaH2PO4_plus2 = Species("LaH2PO4++", None, ["La", "H", "P", "O"], 0.235892741, +2, PhaseType.AQUEOUS)
    LaSO4_plus = Species("LaSO4+", None, ["La", "S", "O"], 0.23496809999999999, +1, PhaseType.AQUEOUS)
    CeCO3_plus = Species("CeCO3+", None, ["Ce", "C", "O"], 0.2001249, +1, PhaseType.AQUEOUS)
    CeHCO3_plus2 = Species("CeHCO3++", None, ["Ce", "H", "C", "O"], 0.20113283999999998, +2, PhaseType.AQUEOUS)
    CeOH_plus2 = Species("CeOH++", None, ["Ce", "O", "H"], 0.15712334, +2, PhaseType.AQUEOUS)
    CeO_plus = Species("CeO+", None, ["Ce", "O"], 0.1561154, +1, PhaseType.AQUEOUS)
    CeO2_minus = Species("CeO2-", None, ["Ce", "O"], 0.1721148, -1, PhaseType.AQUEOUS)
    CeCl_plus2 = Species("CeCl++", None, ["Ce", "Cl"], 0.17556899999999998, +2, PhaseType.AQUEOUS)
    CeCl2_plus = Species("CeCl2+", None, ["Ce", "Cl"], 0.211022, +1, PhaseType.AQUEOUS)
    CeCl4_minus = Species("CeCl4-", None, ["Ce", "Cl"], 0.281928, -1, PhaseType.AQUEOUS)
    CeH2PO4_plus2 = Species("CeH2PO4++", None, ["Ce", "H", "P", "O"], 0.237103241, +2, PhaseType.AQUEOUS)
    CeNO3_plus2 = Species("CeNO3++", None, ["Ce", "N", "O"], 0.2021209, +2, PhaseType.AQUEOUS)
    CeF_plus2 = Species("CeF++", None, ["Ce", "F"], 0.1591144032, +2, PhaseType.AQUEOUS)
    CeF2_plus = Species("CeF2+", None, ["Ce", "F"], 0.17811280640000002, +1, PhaseType.AQUEOUS)
    CeF4_minus = Species("CeF4-", None, ["Ce", "F"], 0.21610961280000002, -1, PhaseType.AQUEOUS)
    CeBr_plus2 = Species("CeBr++", None, ["Ce", "Br"], 0.22002000000000002, +2, PhaseType.AQUEOUS)
    CeIO3_plus2 = Species("CeIO3++", None, ["Ce", "I", "O"], 0.31501867, +2, PhaseType.AQUEOUS)
    CeClO4_plus2 = Species("CeClO4++", None, ["Ce", "Cl", "O"], 0.2395666, +2, PhaseType.AQUEOUS)
    CeSO4_plus = Species("CeSO4+", None, ["Ce", "S", "O"], 0.2361786, +1, PhaseType.AQUEOUS)
    PrCO3_plus = Species("PrCO3+", None, ["Pr", "C", "O"], 0.20091655, +1, PhaseType.AQUEOUS)
    PrHCO3_plus2 = Species("PrHCO3++", None, ["Pr", "H", "C", "O"], 0.20192448999999998, +2, PhaseType.AQUEOUS)
    PrCl_plus2 = Species("PrCl++", None, ["Pr", "Cl"], 0.17636064999999998, +2, PhaseType.AQUEOUS)
    PrCl2_plus = Species("PrCl2+", None, ["Pr", "Cl"], 0.21181365, +1, PhaseType.AQUEOUS)
    PrCl4_minus = Species("PrCl4-", None, ["Pr", "Cl"], 0.28271965, -1, PhaseType.AQUEOUS)
    PrH2PO4_plus2 = Species("PrH2PO4++", None, ["Pr", "H", "P", "O"], 0.237894891, +2, PhaseType.AQUEOUS)
    PrNO3_plus2 = Species("PrNO3++", None, ["Pr", "N", "O"], 0.20291255, +2, PhaseType.AQUEOUS)
    PrF_plus2 = Species("PrF++", None, ["Pr", "F"], 0.1599060532, +2, PhaseType.AQUEOUS)
    PrF2_plus = Species("PrF2+", None, ["Pr", "F"], 0.1789044564, +1, PhaseType.AQUEOUS)
    PrF4_minus = Species("PrF4-", None, ["Pr", "F"], 0.21690126280000002, -1, PhaseType.AQUEOUS)
    PrOH_plus2 = Species("PrOH++", None, ["Pr", "O", "H"], 0.15791498999999998, +2, PhaseType.AQUEOUS)
    PrO_plus = Species("PrO+", None, ["Pr", "O"], 0.15690705, +1, PhaseType.AQUEOUS)
    PrO2_minus = Species("PrO2-", None, ["Pr", "O"], 0.17290645000000002, -1, PhaseType.AQUEOUS)
    PrSO4_plus = Species("PrSO4+", None, ["Pr", "S", "O"], 0.23697025, +1, PhaseType.AQUEOUS)
    NdCO3_plus = Species("NdCO3+", None, ["Nd", "C", "O"], 0.20424889999999998, +1, PhaseType.AQUEOUS)
    NdHCO3_plus2 = Species("NdHCO3++", None, ["Nd", "H", "C", "O"], 0.20525684000000002, +2, PhaseType.AQUEOUS)
    NdOH_plus2 = Species("NdOH++", None, ["Nd", "O", "H"], 0.16124734000000002, +2, PhaseType.AQUEOUS)
    NdO_plus = Species("NdO+", None, ["Nd", "O"], 0.16023939999999998, +1, PhaseType.AQUEOUS)
    NdO2_minus = Species("NdO2-", None, ["Nd", "O"], 0.1762388, -1, PhaseType.AQUEOUS)
    NdCl_plus2 = Species("NdCl++", None, ["Nd", "Cl"], 0.17969300000000002, +2, PhaseType.AQUEOUS)
    NdCl2_plus = Species("NdCl2+", None, ["Nd", "Cl"], 0.21514599999999998, +1, PhaseType.AQUEOUS)
    NdCl4_minus = Species("NdCl4-", None, ["Nd", "Cl"], 0.28605200000000003, -1, PhaseType.AQUEOUS)
    NdH2PO4_plus2 = Species("NdH2PO4++", None, ["Nd", "H", "P", "O"], 0.24122724099999998, +2, PhaseType.AQUEOUS)
    NdNO3_plus2 = Species("NdNO3++", None, ["Nd", "N", "O"], 0.2062449, +2, PhaseType.AQUEOUS)
    NdF_plus2 = Species("NdF++", None, ["Nd", "F"], 0.1632384032, +2, PhaseType.AQUEOUS)
    NdF2_plus = Species("NdF2+", None, ["Nd", "F"], 0.1822368064, +1, PhaseType.AQUEOUS)
    NdF4_minus = Species("NdF4-", None, ["Nd", "F"], 0.2202336128, -1, PhaseType.AQUEOUS)
    NdSO4_plus = Species("NdSO4+", None, ["Nd", "S", "O"], 0.2403026, +1, PhaseType.AQUEOUS)
    SmCO3_plus = Species("SmCO3+", None, ["Sm", "C", "O"], 0.2103689, +1, PhaseType.AQUEOUS)
    SmOH_plus2 = Species("SmOH++", None, ["Sm", "O", "H"], 0.16736734, +2, PhaseType.AQUEOUS)
    SmO_plus = Species("SmO+", None, ["Sm", "O"], 0.1663594, +1, PhaseType.AQUEOUS)
    SmO2_minus = Species("SmO2-", None, ["Sm", "O"], 0.18235880000000002, -1, PhaseType.AQUEOUS)
    SmHCO3_plus2 = Species("SmHCO3++", None, ["Sm", "H", "C", "O"], 0.21137683999999998, +2, PhaseType.AQUEOUS)
    SmCl_plus2 = Species("SmCl++", None, ["Sm", "Cl"], 0.18581299999999998, +2, PhaseType.AQUEOUS)
    SmCl2_plus = Species("SmCl2+", None, ["Sm", "Cl"], 0.221266, +1, PhaseType.AQUEOUS)
    SmCl4_minus = Species("SmCl4-", None, ["Sm", "Cl"], 0.29217200000000004, -1, PhaseType.AQUEOUS)
    SmH2PO4_plus2 = Species("SmH2PO4++", None, ["Sm", "H", "P", "O"], 0.247347241, +2, PhaseType.AQUEOUS)
    SmNO3_plus2 = Species("SmNO3++", None, ["Sm", "N", "O"], 0.2123649, +2, PhaseType.AQUEOUS)
    SmF_plus2 = Species("SmF++", None, ["Sm", "F"], 0.1693584032, +2, PhaseType.AQUEOUS)
    SmF2_plus = Species("SmF2+", None, ["Sm", "F"], 0.18835680640000002, +1, PhaseType.AQUEOUS)
    SmF4_minus = Species("SmF4-", None, ["Sm", "F"], 0.22635361280000002, -1, PhaseType.AQUEOUS)
    SmSO4_plus = Species("SmSO4+", None, ["Sm", "S", "O"], 0.2464226, +1, PhaseType.AQUEOUS)
    EuCO3_plus = Species("EuCO3+", None, ["Eu", "C", "O"], 0.21197290000000002, +1, PhaseType.AQUEOUS)
    EuOH_plus2 = Species("EuOH++", None, ["Eu", "O", "H"], 0.16897134, +2, PhaseType.AQUEOUS)
    EuO_plus = Species("EuO+", None, ["Eu", "O"], 0.1679634, +1, PhaseType.AQUEOUS)
    EuO2_minus = Species("EuO2-", None, ["Eu", "O"], 0.18396279999999998, -1, PhaseType.AQUEOUS)
    EuHCO3_plus2 = Species("EuHCO3++", None, ["Eu", "H", "C", "O"], 0.21298084, +2, PhaseType.AQUEOUS)
    EuCl_plus2 = Species("EuCl++", None, ["Eu", "Cl"], 0.187417, +2, PhaseType.AQUEOUS)
    EuCl2_plus = Species("EuCl2+", None, ["Eu", "Cl"], 0.22287, +1, PhaseType.AQUEOUS)
    EuCl4_minus = Species("EuCl4-", None, ["Eu", "Cl"], 0.29377600000000004, -1, PhaseType.AQUEOUS)
    EuF_plus = Species("EuF+", None, ["Eu", "F"], 0.1709624032, +1, PhaseType.AQUEOUS)
    EuF3_minus = Species("EuF3-", None, ["Eu", "F"], 0.2089592096, -1, PhaseType.AQUEOUS)
    EuF4_minus2 = Species("EuF4--", None, ["Eu", "F"], 0.2279576128, -2, PhaseType.AQUEOUS)
    EuCl_plus = Species("EuCl+", None, ["Eu", "Cl"], 0.187417, +1, PhaseType.AQUEOUS)
    EuCl3_minus = Species("EuCl3-", None, ["Eu", "Cl"], 0.25832299999999997, -1, PhaseType.AQUEOUS)
    EuCl4_minus2 = Species("EuCl4--", None, ["Eu", "Cl"], 0.29377600000000004, -2, PhaseType.AQUEOUS)
    EuH2PO4_plus2 = Species("EuH2PO4++", None, ["Eu", "H", "P", "O"], 0.24895124100000002, +2, PhaseType.AQUEOUS)
    EuNO3_plus2 = Species("EuNO3++", None, ["Eu", "N", "O"], 0.2139689, +2, PhaseType.AQUEOUS)
    EuF_plus2 = Species("EuF++", None, ["Eu", "F"], 0.1709624032, +2, PhaseType.AQUEOUS)
    EuF2_plus = Species("EuF2+", None, ["Eu", "F"], 0.1899608064, +1, PhaseType.AQUEOUS)
    EuF4_minus = Species("EuF4-", None, ["Eu", "F"], 0.2279576128, -1, PhaseType.AQUEOUS)
    EuSO4_plus = Species("EuSO4+", None, ["Eu", "S", "O"], 0.2480266, +1, PhaseType.AQUEOUS)
    GdCO3_plus = Species("GdCO3+", None, ["Gd", "C", "O"], 0.2172589, +1, PhaseType.AQUEOUS)
    GdOH_plus2 = Species("GdOH++", None, ["Gd", "O", "H"], 0.17425734, +2, PhaseType.AQUEOUS)
    GdO_plus = Species("GdO+", None, ["Gd", "O"], 0.1732494, +1, PhaseType.AQUEOUS)
    GdO2_minus = Species("GdO2-", None, ["Gd", "O"], 0.1892488, -1, PhaseType.AQUEOUS)
    GdHCO3_plus2 = Species("GdHCO3++", None, ["Gd", "H", "C", "O"], 0.21826684, +2, PhaseType.AQUEOUS)
    GdCl_plus2 = Species("GdCl++", None, ["Gd", "Cl"], 0.192703, +2, PhaseType.AQUEOUS)
    GdCl2_plus = Species("GdCl2+", None, ["Gd", "Cl"], 0.228156, +1, PhaseType.AQUEOUS)
    GdCl4_minus = Species("GdCl4-", None, ["Gd", "Cl"], 0.299062, -1, PhaseType.AQUEOUS)
    GdH2PO4_plus2 = Species("GdH2PO4++", None, ["Gd", "H", "P", "O"], 0.254237241, +2, PhaseType.AQUEOUS)
    GdNO3_plus2 = Species("GdNO3++", None, ["Gd", "N", "O"], 0.2192549, +2, PhaseType.AQUEOUS)
    GdF_plus2 = Species("GdF++", None, ["Gd", "F"], 0.17624840320000001, +2, PhaseType.AQUEOUS)
    GdF2_plus = Species("GdF2+", None, ["Gd", "F"], 0.1952468064, +1, PhaseType.AQUEOUS)
    GdF4_minus = Species("GdF4-", None, ["Gd", "F"], 0.2332436128, -1, PhaseType.AQUEOUS)
    GdSO4_plus = Species("GdSO4+", None, ["Gd", "S", "O"], 0.2533126, +1, PhaseType.AQUEOUS)
    TbCO3_plus = Species("TbCO3+", None, ["Tb", "C", "O"], 0.21893424, +1, PhaseType.AQUEOUS)
    TbOH_plus2 = Species("TbOH++", None, ["Tb", "O", "H"], 0.17593268, +2, PhaseType.AQUEOUS)
    TbO_plus = Species("TbO+", None, ["Tb", "O"], 0.17492474000000002, +1, PhaseType.AQUEOUS)
    TbO2_minus = Species("TbO2-", None, ["Tb", "O"], 0.19092414, -1, PhaseType.AQUEOUS)
    TbHCO3_plus2 = Species("TbHCO3++", None, ["Tb", "H", "C", "O"], 0.21994218000000001, +2, PhaseType.AQUEOUS)
    TbCl_plus2 = Species("TbCl++", None, ["Tb", "Cl"], 0.19437834, +2, PhaseType.AQUEOUS)
    TbCl2_plus = Species("TbCl2+", None, ["Tb", "Cl"], 0.22983134000000002, +1, PhaseType.AQUEOUS)
    TbCl4_minus = Species("TbCl4-", None, ["Tb", "Cl"], 0.30073734, -1, PhaseType.AQUEOUS)
    TbH2PO4_plus2 = Species("TbH2PO4++", None, ["Tb", "H", "P", "O"], 0.255912581, +2, PhaseType.AQUEOUS)
    TbNO3_plus2 = Species("TbNO3++", None, ["Tb", "N", "O"], 0.22093024, +2, PhaseType.AQUEOUS)
    TbF_plus2 = Species("TbF++", None, ["Tb", "F"], 0.17792374319999998, +2, PhaseType.AQUEOUS)
    TbF2_plus = Species("TbF2+", None, ["Tb", "F"], 0.1969221464, +1, PhaseType.AQUEOUS)
    TbF4_minus = Species("TbF4-", None, ["Tb", "F"], 0.2349189528, -1, PhaseType.AQUEOUS)
    TbSO4_plus = Species("TbSO4+", None, ["Tb", "S", "O"], 0.25498794, +1, PhaseType.AQUEOUS)
    DyCO3_plus = Species("DyCO3+", None, ["Dy", "C", "O"], 0.2225089, +1, PhaseType.AQUEOUS)
    DyHCO3_plus2 = Species("DyHCO3++", None, ["Dy", "H", "C", "O"], 0.22351684, +2, PhaseType.AQUEOUS)
    DyCl_plus2 = Species("DyCl++", None, ["Dy", "Cl"], 0.197953, +2, PhaseType.AQUEOUS)
    DyCl2_plus = Species("DyCl2+", None, ["Dy", "Cl"], 0.233406, +1, PhaseType.AQUEOUS)
    DyCl4_minus = Species("DyCl4-", None, ["Dy", "Cl"], 0.304312, -1, PhaseType.AQUEOUS)
    DyH2PO4_plus2 = Species("DyH2PO4++", None, ["Dy", "H", "P", "O"], 0.259487241, +2, PhaseType.AQUEOUS)
    DyNO3_plus2 = Species("DyNO3++", None, ["Dy", "N", "O"], 0.22450489999999998, +2, PhaseType.AQUEOUS)
    DyF_plus2 = Species("DyF++", None, ["Dy", "F"], 0.18149840320000002, +2, PhaseType.AQUEOUS)
    DyF2_plus = Species("DyF2+", None, ["Dy", "F"], 0.2004968064, +1, PhaseType.AQUEOUS)
    DyF4_minus = Species("DyF4-", None, ["Dy", "F"], 0.2384936128, -1, PhaseType.AQUEOUS)
    DyOH_plus2 = Species("DyOH++", None, ["Dy", "O", "H"], 0.17950734, +2, PhaseType.AQUEOUS)
    DyO_plus = Species("DyO+", None, ["Dy", "O"], 0.1784994, +1, PhaseType.AQUEOUS)
    DyO2_minus = Species("DyO2-", None, ["Dy", "O"], 0.1944988, -1, PhaseType.AQUEOUS)
    DySO4_plus = Species("DySO4+", None, ["Dy", "S", "O"], 0.2585626, +1, PhaseType.AQUEOUS)
    HoCO3_plus = Species("HoCO3+", None, ["Ho", "C", "O"], 0.22493922, +1, PhaseType.AQUEOUS)
    HoHCO3_plus2 = Species("HoHCO3++", None, ["Ho", "H", "C", "O"], 0.22594716, +2, PhaseType.AQUEOUS)
    HoCl_plus2 = Species("HoCl++", None, ["Ho", "Cl"], 0.20038332, +2, PhaseType.AQUEOUS)
    HoCl2_plus = Species("HoCl2+", None, ["Ho", "Cl"], 0.23583632, +1, PhaseType.AQUEOUS)
    HoCl4_minus = Species("HoCl4-", None, ["Ho", "Cl"], 0.30674232, -1, PhaseType.AQUEOUS)
    HoH2PO4_plus2 = Species("HoH2PO4++", None, ["Ho", "H", "P", "O"], 0.26191756099999997, +2, PhaseType.AQUEOUS)
    HoNO3_plus2 = Species("HoNO3++", None, ["Ho", "N", "O"], 0.22693522, +2, PhaseType.AQUEOUS)
    HoF_plus2 = Species("HoF++", None, ["Ho", "F"], 0.1839287232, +2, PhaseType.AQUEOUS)
    HoF2_plus = Species("HoF2+", None, ["Ho", "F"], 0.2029271264, +1, PhaseType.AQUEOUS)
    HoF4_minus = Species("HoF4-", None, ["Ho", "F"], 0.2409239328, -1, PhaseType.AQUEOUS)
    HoOH_plus2 = Species("HoOH++", None, ["Ho", "O", "H"], 0.18193766, +2, PhaseType.AQUEOUS)
    HoO_plus = Species("HoO+", None, ["Ho", "O"], 0.18092972000000002, +1, PhaseType.AQUEOUS)
    HoO2_minus = Species("HoO2-", None, ["Ho", "O"], 0.19692912, -1, PhaseType.AQUEOUS)
    HoSO4_plus = Species("HoSO4+", None, ["Ho", "S", "O"], 0.26099292, +1, PhaseType.AQUEOUS)
    ErCO3_plus = Species("ErCO3+", None, ["Er", "C", "O"], 0.2272679, +1, PhaseType.AQUEOUS)
    ErHCO3_plus2 = Species("ErHCO3++", None, ["Er", "H", "C", "O"], 0.22827583999999998, +2, PhaseType.AQUEOUS)
    ErCl_plus2 = Species("ErCl++", None, ["Er", "Cl"], 0.20271199999999998, +2, PhaseType.AQUEOUS)
    ErCl2_plus = Species("ErCl2+", None, ["Er", "Cl"], 0.238165, +1, PhaseType.AQUEOUS)
    ErCl4_minus = Species("ErCl4-", None, ["Er", "Cl"], 0.30907100000000004, -1, PhaseType.AQUEOUS)
    ErH2PO4_plus2 = Species("ErH2PO4++", None, ["Er", "H", "P", "O"], 0.264246241, +2, PhaseType.AQUEOUS)
    ErNO3_plus2 = Species("ErNO3++", None, ["Er", "N", "O"], 0.22926390000000002, +2, PhaseType.AQUEOUS)
    ErF_plus2 = Species("ErF++", None, ["Er", "F"], 0.1862574032, +2, PhaseType.AQUEOUS)
    ErF2_plus = Species("ErF2+", None, ["Er", "F"], 0.20525580640000002, +1, PhaseType.AQUEOUS)
    ErF4_minus = Species("ErF4-", None, ["Er", "F"], 0.24325261280000002, -1, PhaseType.AQUEOUS)
    ErOH_plus2 = Species("ErOH++", None, ["Er", "O", "H"], 0.18426634, +2, PhaseType.AQUEOUS)
    ErO_plus = Species("ErO+", None, ["Er", "O"], 0.1832584, +1, PhaseType.AQUEOUS)
    ErO2_minus = Species("ErO2-", None, ["Er", "O"], 0.1992578, -1, PhaseType.AQUEOUS)
    ErSO4_plus = Species("ErSO4+", None, ["Er", "S", "O"], 0.2633216, +1, PhaseType.AQUEOUS)
    TmCO3_plus = Species("TmCO3+", None, ["Tm", "C", "O"], 0.22894310999999998, +1, PhaseType.AQUEOUS)
    TmHCO3_plus2 = Species("TmHCO3++", None, ["Tm", "H", "C", "O"], 0.22995105000000002, +2, PhaseType.AQUEOUS)
    TmCl_plus2 = Species("TmCl++", None, ["Tm", "Cl"], 0.20438721, +2, PhaseType.AQUEOUS)
    TmCl2_plus = Species("TmCl2+", None, ["Tm", "Cl"], 0.23984021000000003, +1, PhaseType.AQUEOUS)
    TmCl4_minus = Species("TmCl4-", None, ["Tm", "Cl"], 0.31074621, -1, PhaseType.AQUEOUS)
    TmH2PO4_plus2 = Species("TmH2PO4++", None, ["Tm", "H", "P", "O"], 0.265921451, +2, PhaseType.AQUEOUS)
    TmNO3_plus2 = Species("TmNO3++", None, ["Tm", "N", "O"], 0.23093911, +2, PhaseType.AQUEOUS)
    TmF_plus2 = Species("TmF++", None, ["Tm", "F"], 0.1879326132, +2, PhaseType.AQUEOUS)
    TmF2_plus = Species("TmF2+", None, ["Tm", "F"], 0.2069310164, +1, PhaseType.AQUEOUS)
    TmF4_minus = Species("TmF4-", None, ["Tm", "F"], 0.2449278228, -1, PhaseType.AQUEOUS)
    TmOH_plus2 = Species("TmOH++", None, ["Tm", "O", "H"], 0.18594155, +2, PhaseType.AQUEOUS)
    TmO_plus = Species("TmO+", None, ["Tm", "O"], 0.18493361, +1, PhaseType.AQUEOUS)
    TmO2_minus = Species("TmO2-", None, ["Tm", "O"], 0.20093301, -1, PhaseType.AQUEOUS)
    TmSO4_plus = Species("TmSO4+", None, ["Tm", "S", "O"], 0.26499680999999997, +1, PhaseType.AQUEOUS)
    YbCO3_plus = Species("YbCO3+", None, ["Yb", "C", "O"], 0.2330489, +1, PhaseType.AQUEOUS)
    YbOH_plus2 = Species("YbOH++", None, ["Yb", "O", "H"], 0.19004733999999998, +2, PhaseType.AQUEOUS)
    YbO_plus = Species("YbO+", None, ["Yb", "O"], 0.1890394, +1, PhaseType.AQUEOUS)
    YbO2_minus = Species("YbO2-", None, ["Yb", "O"], 0.20503880000000002, -1, PhaseType.AQUEOUS)
    YbHCO3_plus2 = Species("YbHCO3++", None, ["Yb", "H", "C", "O"], 0.23405684, +2, PhaseType.AQUEOUS)
    YbCl_plus2 = Species("YbCl++", None, ["Yb", "Cl"], 0.20849299999999998, +2, PhaseType.AQUEOUS)
    YbCl2_plus = Species("YbCl2+", None, ["Yb", "Cl"], 0.243946, +1, PhaseType.AQUEOUS)
    YbCl4_minus = Species("YbCl4-", None, ["Yb", "Cl"], 0.31485199999999997, -1, PhaseType.AQUEOUS)
    YbH2PO4_plus2 = Species("YbH2PO4++", None, ["Yb", "H", "P", "O"], 0.27002724100000003, +2, PhaseType.AQUEOUS)
    YbNO3_plus2 = Species("YbNO3++", None, ["Yb", "N", "O"], 0.2350449, +2, PhaseType.AQUEOUS)
    YbF_plus2 = Species("YbF++", None, ["Yb", "F"], 0.1920384032, +2, PhaseType.AQUEOUS)
    YbF2_plus = Species("YbF2+", None, ["Yb", "F"], 0.2110368064, +1, PhaseType.AQUEOUS)
    YbF4_minus = Species("YbF4-", None, ["Yb", "F"], 0.2490336128, -1, PhaseType.AQUEOUS)
    YbSO4_plus = Species("YbSO4+", None, ["Yb", "S", "O"], 0.26910259999999997, +1, PhaseType.AQUEOUS)
    LuCO3_plus = Species("LuCO3+", None, ["Lu", "C", "O"], 0.2349759, +1, PhaseType.AQUEOUS)
    LuOH_plus2 = Species("LuOH++", None, ["Lu", "O", "H"], 0.19197434000000002, +2, PhaseType.AQUEOUS)
    LuO_plus = Species("LuO+", None, ["Lu", "O"], 0.19096639999999998, +1, PhaseType.AQUEOUS)
    LuO2_minus = Species("LuO2-", None, ["Lu", "O"], 0.2069658, -1, PhaseType.AQUEOUS)
    LuHCO3_plus2 = Species("LuHCO3++", None, ["Lu", "H", "C", "O"], 0.23598384, +2, PhaseType.AQUEOUS)
    LuCl_plus2 = Species("LuCl++", None, ["Lu", "Cl"], 0.21042, +2, PhaseType.AQUEOUS)
    LuCl2_plus = Species("LuCl2+", None, ["Lu", "Cl"], 0.24587299999999998, +1, PhaseType.AQUEOUS)
    LuCl4_minus = Species("LuCl4-", None, ["Lu", "Cl"], 0.316779, -1, PhaseType.AQUEOUS)
    LuH2PO4_plus2 = Species("LuH2PO4++", None, ["Lu", "H", "P", "O"], 0.270946301, +2, PhaseType.AQUEOUS)
    LuNO3_plus2 = Species("LuNO3++", None, ["Lu", "N", "O"], 0.2369719, +2, PhaseType.AQUEOUS)
    LuF_plus2 = Species("LuF++", None, ["Lu", "F"], 0.1939654032, +2, PhaseType.AQUEOUS)
    LuF2_plus = Species("LuF2+", None, ["Lu", "F"], 0.2129638064, +1, PhaseType.AQUEOUS)
    LuF4_minus = Species("LuF4-", None, ["Lu", "F"], 0.2509606128, -1, PhaseType.AQUEOUS)
    LuSO4_plus = Species("LuSO4+", None, ["Lu", "S", "O"], 0.27102960000000004, +1, PhaseType.AQUEOUS)
    NaSO4_minus = Species("NaSO4-", None, ["Na", "S", "O"], 0.11905236999999999, -1, PhaseType.AQUEOUS)
    BeCl_plus = Species("BeCl+", None, ["Be", "Cl"], 0.044465182, +1, PhaseType.AQUEOUS)
    FeCl_plus2 = Species("FeCl++", None, ["Fe", "Cl"], 0.091298, +2, PhaseType.AQUEOUS)
    CoCl_plus = Species("CoCl+", None, ["Co", "Cl"], 0.0943862, +1, PhaseType.AQUEOUS)
    CuCl2_minus = Species("CuCl2-", None, ["Cu", "Cl"], 0.134452, -1, PhaseType.AQUEOUS)
    CuCl3_minus2 = Species("CuCl3--", None, ["Cu", "Cl"], 0.169905, -2, PhaseType.AQUEOUS)
    CuCl_plus = Species("CuCl+", None, ["Cu", "Cl"], 0.09899899999999999, +1, PhaseType.AQUEOUS)
    CuCl3_minus = Species("CuCl3-", None, ["Cu", "Cl"], 0.169905, -1, PhaseType.AQUEOUS)
    CuCl4_minus2 = Species("CuCl4--", None, ["Cu", "Cl"], 0.205358, -2, PhaseType.AQUEOUS)
    CdCl_plus = Species("CdCl+", None, ["Cd", "Cl"], 0.147864, +1, PhaseType.AQUEOUS)
    CdCl3_minus = Species("CdCl3-", None, ["Cd", "Cl"], 0.21877000000000002, -1, PhaseType.AQUEOUS)
    CdCl4_minus2 = Species("CdCl4--", None, ["Cd", "Cl"], 0.25422300000000003, -2, PhaseType.AQUEOUS)
    TlCl_plus2 = Species("TlCl++", None, ["Tl", "Cl"], 0.2398363, +2, PhaseType.AQUEOUS)
    AuCl2_minus = Species("AuCl2-", None, ["Au", "Cl"], 0.26787255, -1, PhaseType.AQUEOUS)
    AuCl3_minus2 = Species("AuCl3--", None, ["Au", "Cl"], 0.30332555, -2, PhaseType.AQUEOUS)
    AuCl4_minus = Species("AuCl4-", None, ["Au", "Cl"], 0.33877855, -1, PhaseType.AQUEOUS)
    HgCl_plus = Species("HgCl+", None, ["Hg", "Cl"], 0.236043, +1, PhaseType.AQUEOUS)
    HgCl3_minus = Species("HgCl3-", None, ["Hg", "Cl"], 0.306949, -1, PhaseType.AQUEOUS)
    HgCl4_minus2 = Species("HgCl4--", None, ["Hg", "Cl"], 0.342402, -2, PhaseType.AQUEOUS)
    InCl_plus2 = Species("InCl++", None, ["In", "Cl"], 0.150271, +2, PhaseType.AQUEOUS)
    BeF_plus = Species("BeF+", None, ["Be", "F"], 0.0280105852, +1, PhaseType.AQUEOUS)
    BeF3_minus = Species("BeF3-", None, ["Be", "F"], 0.0660073916, -1, PhaseType.AQUEOUS)
    BeF4_minus2 = Species("BeF4--", None, ["Be", "F"], 0.0850057948, -2, PhaseType.AQUEOUS)
    MnF_plus = Species("MnF+", None, ["Mn", "F"], 0.0739364522, +1, PhaseType.AQUEOUS)
    FeF_plus = Species("FeF+", None, ["Fe", "F"], 0.07484340319999999, +1, PhaseType.AQUEOUS)
    FeF_plus2 = Species("FeF++", None, ["Fe", "F"], 0.07484340319999999, +2, PhaseType.AQUEOUS)
    CoF_plus = Species("CoF+", None, ["Co", "F"], 0.0779316032, +1, PhaseType.AQUEOUS)
    NiF_plus = Species("NiF+", None, ["Ni", "F"], 0.07769180319999999, +1, PhaseType.AQUEOUS)
    CuF_plus = Species("CuF+", None, ["Cu", "F"], 0.0825444032, +1, PhaseType.AQUEOUS)
    ZnF_plus = Species("ZnF+", None, ["Zn", "F"], 0.08440740320000001, +1, PhaseType.AQUEOUS)
    CdF_plus = Species("CdF+", None, ["Cd", "F"], 0.13140940320000002, +1, PhaseType.AQUEOUS)
    BaF_plus = Species("BaF+", None, ["Ba", "F"], 0.15632540320000002, +1, PhaseType.AQUEOUS)
    HgF_plus = Species("HgF+", None, ["Hg", "F"], 0.21958840319999998, +1, PhaseType.AQUEOUS)
    InF_plus2 = Species("InF++", None, ["In", "F"], 0.1338164032, +2, PhaseType.AQUEOUS)
    PbF_plus = Species("PbF+", None, ["Pb", "F"], 0.2261984032, +1, PhaseType.AQUEOUS)
    Ag_HS_2_minus = Species("Ag(HS)2-", None, ["Ag", "H", "S"], 0.17401408000000002, -1, PhaseType.AQUEOUS)
    Au_HS_2_minus = Species("Au(HS)2-", None, ["Au", "H", "S"], 0.26311243, -1, PhaseType.AQUEOUS)
    Pb_HS_3_minus = Species("Pb(HS)3-", None, ["Pb", "H", "S"], 0.30641882, -1, PhaseType.AQUEOUS)
    Mg_HSiO3_plus = Species("Mg(HSiO3)+", None, ["Mg", "H", "Si", "O"], 0.10139664000000001, +1, PhaseType.AQUEOUS)
    Ca_HSiO3_plus = Species("Ca(HSiO3)+", None, ["Ca", "H", "Si", "O"], 0.11716964, +1, PhaseType.AQUEOUS)

    # reaktoro minerals
    Akermanite = Species("Akermanite", None, ["Ca", "Mg", "Si", "O"], 0.2726278, +0, PhaseType.MINERAL)
    Alabandite = Species("Alabandite", None, ["Mn", "S"], 0.087003049, +0, PhaseType.MINERAL)
    Albite_low = Species("Albite,low", None, ["Na", "Al", "Si", "O"], 0.262223008, +0, PhaseType.MINERAL)
    Alunite = Species("Alunite", None, ["K", "Al", "S", "O", "H"], 0.414212154, +0, PhaseType.MINERAL)
    Amesite_7A = Species("Amesite,7A", None, ["Mg", "Al", "Si", "O", "H"], 0.278684936, +0, PhaseType.MINERAL)
    Amorphous_Silica = Species("Amorphous-Silica", None, ["Si", "O"], 0.0600843, +0, PhaseType.MINERAL)
    Analcime = Species("Analcime", None, ["Na", "Al", "Si", "O", "H"], 0.220153988, +0, PhaseType.MINERAL)
    Analcime_dehydrated = Species("Analcime,dehydrated", None, ["Na", "Al", "Si", "O"], 0.202138708, +0, PhaseType.MINERAL)
    Andalusite = Species("Andalusite", None, ["Al", "Si", "O"], 0.16204557600000002, +0, PhaseType.MINERAL)
    Andradite = Species("Andradite", None, ["Ca", "Fe", "Si", "O"], 0.5081732999999999, +0, PhaseType.MINERAL)
    Anglesite = Species("Anglesite", None, ["Pb", "S", "O"], 0.3032626, +0, PhaseType.MINERAL)
    Anhydrite = Species("Anhydrite", None, ["Ca", "S", "O"], 0.1361406, +0, PhaseType.MINERAL)
    Annite = Species("Annite", None, ["K", "Fe", "Al", "Si", "O", "H"], 0.511880018, +0, PhaseType.MINERAL)
    Anorthite = Species("Anorthite", None, ["Ca", "Al", "Si", "O"], 0.278207276, +0, PhaseType.MINERAL)
    Aragonite = Species("Aragonite", None, ["Ca", "C", "O"], 0.1000869, +0, PhaseType.MINERAL)
    Artinite = Species("Artinite", None, ["Mg", "C", "O", "H"], 0.19667942, +0, PhaseType.MINERAL)
    Azurite = Species("Azurite", None, ["Cu", "C", "O", "H"], 0.34467048, +0, PhaseType.MINERAL)
    Barite = Species("Barite", None, ["Ba", "S", "O"], 0.2333896, +0, PhaseType.MINERAL)
    Berndtite = Species("Berndtite", None, ["Sn", "S"], 0.18284, +0, PhaseType.MINERAL)
    Boehmite = Species("Boehmite", None, ["Al", "O", "H"], 0.059988278, +0, PhaseType.MINERAL)
    Bromellite = Species("Bromellite", None, ["Be", "O"], 0.025011582, +0, PhaseType.MINERAL)
    Brucite = Species("Brucite", None, ["Mg", "O", "H"], 0.05831968, +0, PhaseType.MINERAL)
    Ca_Al_Pyroxene = Species("Ca-Al-Pyroxene", None, ["Ca", "Al", "Si", "O"], 0.218122976, +0, PhaseType.MINERAL)
    Calcite = Species("Calcite", None, ["Ca", "C", "O"], 0.1000869, +0, PhaseType.MINERAL)
    Cassiterite = Species("Cassiterite", None, ["Sn", "O"], 0.1507088, +0, PhaseType.MINERAL)
    Celadonite = Species("Celadonite", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.396735518, +0, PhaseType.MINERAL)
    Celestite = Species("Celestite", None, ["Sr", "S", "O"], 0.1836826, +0, PhaseType.MINERAL)
    Cerussite = Species("Cerussite", None, ["Pb", "C", "O"], 0.2672089, +0, PhaseType.MINERAL)
    Chabazite = Species("Chabazite", None, ["Ca", "Al", "Si", "O", "H"], 0.506467556, +0, PhaseType.MINERAL)
    Chalcedony = Species("Chalcedony", None, ["Si", "O"], 0.0600843, +0, PhaseType.MINERAL)
    Chlorargyrite = Species("Chlorargyrite", None, ["Ag", "Cl"], 0.1433212, +0, PhaseType.MINERAL)
    Chloritoid = Species("Chloritoid", None, ["Fe", "Al", "Si", "O", "H"], 0.251905256, +0, PhaseType.MINERAL)
    Chrysotile = Species("Chrysotile", None, ["Mg", "Si", "O", "H"], 0.27711236, +0, PhaseType.MINERAL)
    Cinnabar = Species("Cinnabar", None, ["Hg", "S"], 0.232655, +0, PhaseType.MINERAL)
    Clinochlore_14A = Species("Clinochlore,14A", None, ["Mg", "Al", "Si", "O", "H"], 0.5557972959999999, +0, PhaseType.MINERAL)
    Clinozoisite = Species("Clinozoisite", None, ["Ca", "Al", "Si", "O", "H"], 0.454357254, +0, PhaseType.MINERAL)
    Copper = Species("Copper", None, ["Cu"], 0.063546, +0, PhaseType.MINERAL)
    Cordierite = Species("Cordierite", None, ["Mg", "Al", "Si", "O"], 0.584952852, +0, PhaseType.MINERAL)
    Cordierite_hydrous = Species("Cordierite,hydrous", None, ["Mg", "Al", "Si", "O", "H"], 0.602968132, +0, PhaseType.MINERAL)
    Corundum = Species("Corundum", None, ["Al", "O"], 0.101961276, +0, PhaseType.MINERAL)
    Covellite = Species("Covellite", None, ["Cu", "S"], 0.095611, +0, PhaseType.MINERAL)
    Cristobalite_alpha = Species("Cristobalite,alpha", None, ["Si", "O"], 0.0600843, +0, PhaseType.MINERAL)
    Cristobalite_beta = Species("Cristobalite,beta", None, ["Si", "O"], 0.0600843, +0, PhaseType.MINERAL)
    Cummingtonite = Species("Cummingtonite", None, ["Mg", "Si", "O", "H"], 0.7808204799999999, +0, PhaseType.MINERAL)
    Cuprite = Species("Cuprite", None, ["Cu", "O"], 0.14309139999999998, +0, PhaseType.MINERAL)
    Daphnite_14A = Species("Daphnite,14A", None, ["Fe", "Al", "Si", "O", "H"], 0.713497296, +0, PhaseType.MINERAL)
    Diaspore = Species("Diaspore", None, ["Al", "O", "H"], 0.059988278, +0, PhaseType.MINERAL)
    Dickite = Species("Dickite", None, ["Al", "Si", "O", "H"], 0.258160436, +0, PhaseType.MINERAL)
    Diopside = Species("Diopside", None, ["Ca", "Mg", "Si", "O"], 0.2165504, +0, PhaseType.MINERAL)
    Dolomite = Species("Dolomite", None, ["Ca", "Mg", "C", "O"], 0.1844008, +0, PhaseType.MINERAL)
    Dolomite_dis = Species("Dolomite,dis", None, ["Ca", "Mg", "C", "O"], 0.1844008, +0, PhaseType.MINERAL)
    Dolomite_ord = Species("Dolomite,ord", None, ["Ca", "Mg", "C", "O"], 0.1844008, +0, PhaseType.MINERAL)
    Epidote = Species("Epidote", None, ["Ca", "Fe", "Al", "Si", "O", "H"], 0.483220716, +0, PhaseType.MINERAL)
    Epidote_ord = Species("Epidote,ord", None, ["Ca", "Fe", "Al", "Si", "O", "H"], 0.483220716, +0, PhaseType.MINERAL)
    Fayalite = Species("Fayalite", None, ["Fe", "Si", "O"], 0.2037731, +0, PhaseType.MINERAL)
    Ferropargasite = Species("Ferropargasite", None, ["Na", "Ca", "Fe", "Al", "Si", "O", "H"], 0.961984864, +0, PhaseType.MINERAL)
    Ferrotremolite = Species("Ferrotremolite", None, ["Ca", "Fe", "Si", "O", "H"], 0.97006648, +0, PhaseType.MINERAL)
    Ferrous_Oxide = Species("Ferrous-Oxide", None, ["Fe", "O"], 0.07184439999999999, +0, PhaseType.MINERAL)
    Fluorite = Species("Fluorite", None, ["Ca", "F"], 0.0780748064, +0, PhaseType.MINERAL)
    Fluorphlogopite = Species("Fluorphlogopite", None, ["K", "Mg", "Al", "Si", "O", "F"], 0.42124214439999996, +0, PhaseType.MINERAL)
    Fluortremolite = Species("Fluortremolite", None, ["Ca", "Mg", "Si", "O", "F"], 0.8163486064, +0, PhaseType.MINERAL)
    Forsterite = Species("Forsterite", None, ["Mg", "Si", "O"], 0.1406931, +0, PhaseType.MINERAL)
    Galena = Species("Galena", None, ["Pb", "S"], 0.23926499999999998, +0, PhaseType.MINERAL)
    Gehlenite = Species("Gehlenite", None, ["Ca", "Al", "Si", "O"], 0.274200376, +0, PhaseType.MINERAL)
    Gibbsite = Species("Gibbsite", None, ["Al", "O", "H"], 0.078003558, +0, PhaseType.MINERAL)
    Glaucophane = Species("Glaucophane", None, ["Na", "Mg", "Al", "Si", "O", "H"], 0.7835430959999999, +0, PhaseType.MINERAL)
    Gold = Species("Gold", None, ["Au"], 0.19696655000000002, +0, PhaseType.MINERAL)
    Graphite = Species("Graphite", None, ["C"], 0.0120107, +0, PhaseType.MINERAL)
    Greenalite = Species("Greenalite", None, ["Fe", "Si", "O", "H"], 0.37173236000000004, +0, PhaseType.MINERAL)
    Grossular = Species("Grossular", None, ["Ca", "Al", "Si", "O"], 0.450446376, +0, PhaseType.MINERAL)
    Grunerite = Species("Grunerite", None, ["Fe", "Si", "O", "H"], 1.00160048, +0, PhaseType.MINERAL)
    Halite = Species("Halite", None, ["Na", "Cl"], 0.058442770000000005, +0, PhaseType.MINERAL)
    Halloysite = Species("Halloysite", None, ["Al", "Si", "O", "H"], 0.258160436, +0, PhaseType.MINERAL)
    Hedenbergite = Species("Hedenbergite", None, ["Ca", "Fe", "Si", "O"], 0.2480904, +0, PhaseType.MINERAL)
    Huntite = Species("Huntite", None, ["Ca", "Mg", "C", "O"], 0.35302859999999997, +0, PhaseType.MINERAL)
    Hydromagnesite = Species("Hydromagnesite", None, ["Mg", "C", "O", "H"], 0.4676364, +0, PhaseType.MINERAL)
    Jadeite = Species("Jadeite", None, ["Na", "Al", "Si", "O"], 0.202138708, +0, PhaseType.MINERAL)
    K_Feldspar = Species("K-Feldspar", None, ["K", "Al", "Si", "O"], 0.27833153800000004, +0, PhaseType.MINERAL)
    Kaolinite = Species("Kaolinite", None, ["Al", "Si", "O", "H"], 0.258160436, +0, PhaseType.MINERAL)
    Kyanite = Species("Kyanite", None, ["Al", "Si", "O"], 0.16204557600000002, +0, PhaseType.MINERAL)
    Laurite = Species("Laurite", None, ["Ru", "S"], 0.16519999999999999, +0, PhaseType.MINERAL)
    Laumontite = Species("Laumontite", None, ["Ca", "Al", "Si", "O", "H"], 0.470436996, +0, PhaseType.MINERAL)
    Leonhardite = Species("Leonhardite", None, ["Ca", "Al", "Si", "O", "H"], 0.9228587119999999, +0, PhaseType.MINERAL)
    Lime = Species("Lime", None, ["Ca", "O"], 0.0560774, +0, PhaseType.MINERAL)
    Magnesite = Species("Magnesite", None, ["Mg", "C", "O"], 0.0843139, +0, PhaseType.MINERAL)
    Malachite = Species("Malachite", None, ["Cu", "C", "O", "H"], 0.22111558, +0, PhaseType.MINERAL)
    Manganosite = Species("Manganosite", None, ["Mn", "O"], 0.070937449, +0, PhaseType.MINERAL)
    Merwinite = Species("Merwinite", None, ["Ca", "Mg", "Si", "O"], 0.3287052, +0, PhaseType.MINERAL)
    Metacinnabar = Species("Metacinnabar", None, ["Hg", "S"], 0.232655, +0, PhaseType.MINERAL)
    Microcline_maximum = Species("Microcline,maximum", None, ["K", "Al", "Si", "O"], 0.27833153800000004, +0, PhaseType.MINERAL)
    Minnesotaite = Species("Minnesotaite", None, ["Fe", "Si", "O", "H"], 0.47388568, +0, PhaseType.MINERAL)
    Monticellite = Species("Monticellite", None, ["Ca", "Mg", "Si", "O"], 0.15646610000000002, +0, PhaseType.MINERAL)
    Muscovite = Species("Muscovite", None, ["K", "Al", "Si", "O", "H"], 0.398308094, +0, PhaseType.MINERAL)
    Nepheline = Species("Nepheline", None, ["Na", "Al", "Si", "O"], 0.142054408, +0, PhaseType.MINERAL)
    Palladium = Species("Palladium", None, ["Pd"], 0.10642, +0, PhaseType.MINERAL)
    Paragonite = Species("Paragonite", None, ["Na", "Al", "Si", "O", "H"], 0.382199564, +0, PhaseType.MINERAL)
    Pargasite = Species("Pargasite", None, ["Na", "Ca", "Mg", "Al", "Si", "O", "H"], 0.835824864, +0, PhaseType.MINERAL)
    Periclase = Species("Periclase", None, ["Mg", "O"], 0.040304400000000004, +0, PhaseType.MINERAL)
    Phlogopite = Species("Phlogopite", None, ["K", "Mg", "Al", "Si", "O", "H"], 0.417260018, +0, PhaseType.MINERAL)
    Platinum = Species("Platinum", None, ["Pt"], 0.195078, +0, PhaseType.MINERAL)
    Potassium_Oxide = Species("Potassium-Oxide", None, ["K", "O"], 0.094196, +0, PhaseType.MINERAL)
    Pyrite = Species("Pyrite", None, ["Fe", "S"], 0.119975, +0, PhaseType.MINERAL)
    Pyrophyllite = Species("Pyrophyllite", None, ["Al", "Si", "O", "H"], 0.360313756, +0, PhaseType.MINERAL)
    Pd_OH_2 = Species("Pd(OH2", None, ["Pd", "O", "H"], 0.14043467999999998, +0, PhaseType.MINERAL)
    Pd4S = Species("Pd4S", None, ["Pd", "S"], 0.457745, +0, PhaseType.MINERAL)
    PdO = Species("PdO", None, ["Pd", "O"], 0.1224194, +0, PhaseType.MINERAL)
    PdS = Species("PdS", None, ["Pd", "S"], 0.13848500000000002, +0, PhaseType.MINERAL)
    PtS = Species("PtS", None, ["Pt", "S"], 0.227143, +0, PhaseType.MINERAL)
    PtS2 = Species("PtS2", None, ["Pt", "S"], 0.25920800000000005, +0, PhaseType.MINERAL)
    Rhodium = Species("Rhodium", None, ["Rh"], 0.1029055, +0, PhaseType.MINERAL)
    Rhodochrosite = Species("Rhodochrosite", None, ["Mn", "C", "O"], 0.114946949, +0, PhaseType.MINERAL)
    Richterite = Species("Richterite", None, ["Na", "Ca", "Mg", "Si", "O", "H"], 0.81826802, +0, PhaseType.MINERAL)
    Romarchite = Species("Romarchite", None, ["Sn", "O"], 0.13470939999999998, +0, PhaseType.MINERAL)
    Ruthenium = Species("Ruthenium", None, ["Ru"], 0.10107, +0, PhaseType.MINERAL)
    Rutile = Species("Rutile", None, ["Ti", "O"], 0.07986579999999999, +0, PhaseType.MINERAL)
    Rh2O = Species("Rh2O", None, ["Rh", "O"], 0.2218104, +0, PhaseType.MINERAL)
    Rh2O3 = Species("Rh2O3", None, ["Rh", "O"], 0.2538092, +0, PhaseType.MINERAL)
    RuO2 = Species("RuO2", None, ["Ru", "O"], 0.13306880000000001, +0, PhaseType.MINERAL)
    Sanidine_high = Species("Sanidine,high", None, ["K", "Al", "Si", "O"], 0.27833153800000004, +0, PhaseType.MINERAL)
    Sepiolite = Species("Sepiolite", None, ["Mg", "Si", "O", "H"], 0.64783036, +0, PhaseType.MINERAL)
    Siderite = Species("Siderite", None, ["Fe", "C", "O"], 0.1158539, +0, PhaseType.MINERAL)
    Sillimanite = Species("Sillimanite", None, ["Al", "Si", "O"], 0.16204557600000002, +0, PhaseType.MINERAL)
    Silver = Species("Silver", None, ["Ag"], 0.1078682, +0, PhaseType.MINERAL)
    Smithsonite = Species("Smithsonite", None, ["Zn", "C", "O"], 0.1254179, +0, PhaseType.MINERAL)
    Sodium_Oxide = Species("Sodium-Oxide", None, ["Na", "O"], 0.06197894, +0, PhaseType.MINERAL)
    Sphalerite = Species("Sphalerite", None, ["Zn", "S"], 0.097474, +0, PhaseType.MINERAL)
    Spinel = Species("Spinel", None, ["Mg", "Al", "O"], 0.142265676, +0, PhaseType.MINERAL)
    Staurolite = Species("Staurolite", None, ["Fe", "Al", "Si", "O", "H"], 0.851859382, +0, PhaseType.MINERAL)
    Strontianite = Species("Strontianite", None, ["Sr", "C", "O"], 0.14762889999999998, +0, PhaseType.MINERAL)
    Sylvite = Species("Sylvite", None, ["K", "Cl"], 0.0745513, +0, PhaseType.MINERAL)
    Talc = Species("Talc", None, ["Mg", "Si", "O", "H"], 0.37926568, +0, PhaseType.MINERAL)
    Tenorite = Species("Tenorite", None, ["Cu", "O"], 0.0795454, +0, PhaseType.MINERAL)
    Titanite = Species("Titanite", None, ["Ca", "Ti", "Si", "O"], 0.1960275, +0, PhaseType.MINERAL)
    Tremolite = Species("Tremolite", None, ["Ca", "Mg", "Si", "O", "H"], 0.81236648, +0, PhaseType.MINERAL)
    Uraninite = Species("Uraninite", None, ["U", "O"], 0.27002771000000003, +0, PhaseType.MINERAL)
    PdS2 = Species("PdS2", None, ["Pd", "S"], 0.17055, +0, PhaseType.MINERAL)
    Wairakite = Species("Wairakite", None, ["Ca", "Al", "Si", "O", "H"], 0.434406436, +0, PhaseType.MINERAL)
    Wollastonite = Species("Wollastonite", None, ["Ca", "Si", "O"], 0.11616169999999999, +0, PhaseType.MINERAL)
    Wurtzite = Species("Wurtzite", None, ["Zn", "S"], 0.097474, +0, PhaseType.MINERAL)
    Zincite = Species("Zincite", None, ["Zn", "O"], 0.0814084, +0, PhaseType.MINERAL)
    Zoisite = Species("Zoisite", None, ["Ca", "Al", "Si", "O", "H"], 0.454357254, +0, PhaseType.MINERAL)
    Litharge = Species("Litharge", None, ["Pb", "O"], 0.2231994, +0, PhaseType.MINERAL)
    Albite = Species("Albite", None, ["Na", "Al", "Si", "O"], 0.262223008, +0, PhaseType.MINERAL)
    Albite_high = Species("Albite,high", None, ["Na", "Al", "Si", "O"], 0.262223008, +0, PhaseType.MINERAL)
    Almandine = Species("Almandine", None, ["Fe", "Al", "Si", "O"], 0.49774737599999996, +0, PhaseType.MINERAL)
    Amesite_14A = Species("Amesite,14A", None, ["Mg", "Al", "Si", "O", "H"], 0.557369872, +0, PhaseType.MINERAL)
    Antigorite = Species("Antigorite", None, ["Mg", "Si", "O", "H"], 4.53595108, +0, PhaseType.MINERAL)
    Clinochlore_7A = Species("Clinochlore,7A", None, ["Mg", "Al", "Si", "O", "H"], 0.5557972959999999, +0, PhaseType.MINERAL)
    Coesite = Species("Coesite", None, ["Si", "O"], 0.0600843, +0, PhaseType.MINERAL)
    Cristobalite = Species("Cristobalite", None, ["Si", "O"], 0.0600843, +0, PhaseType.MINERAL)
    Daphnite_7A = Species("Daphnite,7A", None, ["Fe", "Al", "Si", "O", "H"], 0.713497296, +0, PhaseType.MINERAL)
    Edenite = Species("Edenite", None, ["Na", "Ca", "Mg", "Al", "Si", "O", "H"], 0.8342522880000001, +0, PhaseType.MINERAL)
    Epistilbite = Species("Epistilbite", None, ["Ca", "Al", "Si", "O", "H"], 0.6086208759999999, +0, PhaseType.MINERAL)
    Ferroedenite = Species("Ferroedenite", None, ["Na", "Ca", "Fe", "Al", "Si", "O", "H"], 0.9919522879999999, +0, PhaseType.MINERAL)
    Ferrosilite = Species("Ferrosilite", None, ["Fe", "Si", "O"], 0.13192869999999998, +0, PhaseType.MINERAL)
    Fluoredenite = Species("Fluoredenite", None, ["Na", "Ca", "Mg", "Al", "Si", "O", "F"], 0.8382344144, +0, PhaseType.MINERAL)
    Heulandite = Species("Heulandite", None, ["Ca", "Al", "Si", "O", "H"], 0.686720456, +0, PhaseType.MINERAL)
    Kalsilite = Species("Kalsilite", None, ["K", "Al", "Si", "O"], 0.158162938, +0, PhaseType.MINERAL)
    Lawsonite = Species("Lawsonite", None, ["Ca", "Al", "Si", "O", "H"], 0.314237836, +0, PhaseType.MINERAL)
    Magnetite = Species("Magnetite", None, ["Fe", "O"], 0.2315326, +0, PhaseType.MINERAL)
    Margarite = Species("Margarite", None, ["Ca", "Al", "Si", "O", "H"], 0.398183832, +0, PhaseType.MINERAL)
    Natrolite = Species("Natrolite", None, ["Na", "Al", "Si", "O", "H"], 0.380223676, +0, PhaseType.MINERAL)
    Nesquehonite = Species("Nesquehonite", None, ["Mg", "C", "O", "H"], 0.13835973999999998, +0, PhaseType.MINERAL)
    Nickel = Species("Nickel", None, ["Ni"], 0.0586934, +0, PhaseType.MINERAL)
    Phillipsite_Ca = Species("Phillipsite,Ca", None, ["Ca", "Al", "Si", "O", "H"], 0.5485365759999999, +0, PhaseType.MINERAL)
    Phillipsite_K = Species("Phillipsite,K", None, ["K", "Al", "Si", "O", "H"], 0.586655176, +0, PhaseType.MINERAL)
    Phillipsite_Na = Species("Phillipsite,Na", None, ["Na", "Al", "Si", "O", "H"], 0.554438116, +0, PhaseType.MINERAL)
    Prehnite = Species("Prehnite", None, ["Ca", "Al", "Si", "O", "H"], 0.412384256, +0, PhaseType.MINERAL)
    Pyrope = Species("Pyrope", None, ["Mg", "Al", "Si", "O"], 0.40312737600000004, +0, PhaseType.MINERAL)
    Quartz = Species("Quartz", None, ["Si", "O"], 0.0600843, +0, PhaseType.MINERAL)
    Quicksilver = Species("Quicksilver", None, ["Hg"], 0.20059, +0, PhaseType.MINERAL)
    Spessartine = Species("Spessartine", None, ["Mn", "Al", "Si", "O"], 0.495026523, +0, PhaseType.MINERAL)
    Stilbite = Species("Stilbite", None, ["Na", "Ca", "Al", "Si", "O", "H"], 1.4313572799999998, +0, PhaseType.MINERAL)
    Tin = Species("Tin", None, ["Sn"], 0.11871, +0, PhaseType.MINERAL)
    Acanthite = Species("Acanthite", None, ["Ag", "S"], 0.2478014, +0, PhaseType.MINERAL)
    Aegerine = Species("Aegerine", None, ["Na", "Fe", "Si", "O"], 0.23100217, +0, PhaseType.MINERAL)
    Anthophyllite = Species("Anthophyllite", None, ["Mg", "Si", "O", "H"], 0.7808204799999999, +0, PhaseType.MINERAL)
    Bornite = Species("Bornite", None, ["Cu", "Fe", "S"], 0.501835, +0, PhaseType.MINERAL)
    Bunsenite = Species("Bunsenite", None, ["Ni", "O"], 0.0746928, +0, PhaseType.MINERAL)
    Chalcocite = Species("Chalcocite", None, ["Cu", "S"], 0.15915700000000002, +0, PhaseType.MINERAL)
    Chalcopyrite = Species("Chalcopyrite", None, ["Cu", "Fe", "S"], 0.183521, +0, PhaseType.MINERAL)
    Cronstedtite_7A = Species("Cronstedtite,7A", None, ["Fe", "Si", "O", "H"], 0.39949186, +0, PhaseType.MINERAL)
    Enstatite = Species("Enstatite", None, ["Mg", "Si", "O"], 0.1003887, +0, PhaseType.MINERAL)
    Ferrogedrite = Species("Ferrogedrite", None, ["Fe", "Al", "Si", "O", "H"], 0.941665632, +0, PhaseType.MINERAL)
    Hastingsite = Species("Hastingsite", None, ["Na", "Ca", "Fe", "Al", "Si", "O", "H"], 0.9908483260000001, +0, PhaseType.MINERAL)
    Hematite = Species("Hematite", None, ["Fe", "O"], 0.1596882, +0, PhaseType.MINERAL)
    Larnite = Species("Larnite", None, ["Ca", "Si", "O"], 0.1722391, +0, PhaseType.MINERAL)
    Magnesiohastingsite = Species("Magnesiohastingsite", None, ["Na", "Ca", "Mg", "Fe", "Al", "Si", "O", "H"], 0.864688326, +0, PhaseType.MINERAL)
    Magnesioriebeckite = Species("Magnesioriebeckite", None, ["Na", "Mg", "Fe", "Si", "O", "H"], 0.8412700200000001, +0, PhaseType.MINERAL)
    Pyrrhotite = Species("Pyrrhotite", None, ["Fe", "S"], 0.08791, +0, PhaseType.MINERAL)
    Riebeckite = Species("Riebeckite", None, ["Na", "Fe", "Si", "O", "H"], 0.9358900200000001, +0, PhaseType.MINERAL)
    Sulfur = Species("Sulfur", None, ["S"], 0.032064999999999996, +0, PhaseType.MINERAL)
    Pd_Oxyannite = Species("Pd-Oxyannite", None, ["K", "Fe", "Al", "Si", "O", "H"], 0.510872078, +0, PhaseType.MINERAL)

    # reaktoro aqueous species
    AgCl_aq = Species("AgCl(aq)", None, ["Ag", "Cl"], 0.1433212, +0, PhaseType.AQUEOUS)
    AgOH_aq = Species("AgOH(aq)", None, ["Ag", "O", "H"], 0.12487554000000001, +0, PhaseType.AQUEOUS)
    AgNO3_aq = Species("AgNO3(aq)", None, ["Ag", "N", "O"], 0.1698731, +0, PhaseType.AQUEOUS)
    HAlO2_aq = Species("HAlO2(aq)", None, ["H", "Al", "O"], 0.059988278, +0, PhaseType.AQUEOUS)
    B_OH_3_aq = Species("B(OH3(aq)", None, ["B", "O", "H"], 0.061833019999999995, +0, PhaseType.AQUEOUS)
    BeO_aq = Species("BeO(aq)", None, ["Be", "O"], 0.025011582, +0, PhaseType.AQUEOUS)
    HBrO_aq = Species("HBrO(aq)", None, ["H", "Br", "O"], 0.09691134, +0, PhaseType.AQUEOUS)
    HCN_aq = Species("HCN(aq)", None, ["H", "C", "N"], 0.02702534, +0, PhaseType.AQUEOUS)
    CO_aq = Species("CO(aq)", None, ["C", "O"], 0.028010100000000003, +0, PhaseType.AQUEOUS)
    CO2_aq = Species("CO2(aq)", None, ["C", "O"], 0.0440095, +0, PhaseType.AQUEOUS)
    CaCl2_aq = Species("CaCl2(aq)", None, ["Ca", "Cl"], 0.110984, +0, PhaseType.AQUEOUS)
    CaSO4_aq = Species("CaSO4(aq)", None, ["Ca", "S", "O"], 0.1361406, +0, PhaseType.AQUEOUS)
    CdO_aq = Species("CdO(aq)", None, ["Cd", "O"], 0.1284104, +0, PhaseType.AQUEOUS)
    HClO_aq = Species("HClO(aq)", None, ["H", "Cl", "O"], 0.05246034, +0, PhaseType.AQUEOUS)
    CoO_aq = Species("CoO(aq)", None, ["Co", "O"], 0.07493259999999999, +0, PhaseType.AQUEOUS)
    CsBr_aq = Species("CsBr(aq)", None, ["Cs", "Br"], 0.21280945, +0, PhaseType.AQUEOUS)
    CsCl_aq = Species("CsCl(aq)", None, ["Cs", "Cl"], 0.16835845, +0, PhaseType.AQUEOUS)
    CsI_aq = Species("CsI(aq)", None, ["Cs", "I"], 0.25980991999999997, +0, PhaseType.AQUEOUS)
    CsOH_aq = Species("CsOH(aq)", None, ["Cs", "O", "H"], 0.14991279, +0, PhaseType.AQUEOUS)
    CuO_aq = Species("CuO(aq)", None, ["Cu", "O"], 0.0795454, +0, PhaseType.AQUEOUS)
    FeCl2_aq = Species("FeCl2(aq)", None, ["Fe", "Cl"], 0.126751, +0, PhaseType.AQUEOUS)
    FeO_aq = Species("FeO(aq)", None, ["Fe", "O"], 0.07184439999999999, +0, PhaseType.AQUEOUS)
    HFeO2_aq = Species("HFeO2(aq)", None, ["H", "Fe", "O"], 0.08885174000000001, +0, PhaseType.AQUEOUS)
    HGaO2_aq = Species("HGaO2(aq)", None, ["H", "Ga", "O"], 0.10272974, +0, PhaseType.AQUEOUS)
    H2_aq = Species("H2(aq)", None, ["H"], 0.0020158800000000003, +0, PhaseType.AQUEOUS)
    H2S_aq = Species("H2S(aq)", None, ["H", "S"], 0.03408088, +0, PhaseType.AQUEOUS)
    H3VO4_aq = Species("H3VO4(aq)", None, ["H", "V", "O"], 0.11796292, +0, PhaseType.AQUEOUS)
    H3PO4_aq = Species("H3PO4(aq)", None, ["H", "P", "O"], 0.097995181, +0, PhaseType.AQUEOUS)
    HF_aq = Species("HF(aq)", None, ["H", "F"], 0.0200063432, +0, PhaseType.AQUEOUS)
    HNO3_aq = Species("HNO3(aq)", None, ["H", "N", "O"], 0.06301284, +0, PhaseType.AQUEOUS)
    H2SeO3_aq = Species("H2SeO3(aq)", None, ["H", "Se", "O"], 0.12897408, +0, PhaseType.AQUEOUS)
    He_aq = Species("He(aq)", None, ["He"], 0.004002602, +0, PhaseType.AQUEOUS)
    HgO_aq = Species("HgO(aq)", None, ["Hg", "O"], 0.21658940000000002, +0, PhaseType.AQUEOUS)
    HIO_aq = Species("HIO(aq)", None, ["H", "I", "O"], 0.14391181, +0, PhaseType.AQUEOUS)
    HInO2_aq = Species("HInO2(aq)", None, ["H", "In", "O"], 0.14782473999999998, +0, PhaseType.AQUEOUS)
    KBr_aq = Species("KBr(aq)", None, ["K", "Br"], 0.1190023, +0, PhaseType.AQUEOUS)
    KCl_aq = Species("KCl(aq)", None, ["K", "Cl"], 0.0745513, +0, PhaseType.AQUEOUS)
    KHSO4_aq = Species("KHSO4(aq)", None, ["K", "H", "S", "O"], 0.13616883999999999, +0, PhaseType.AQUEOUS)
    KI_aq = Species("KI(aq)", None, ["K", "I"], 0.16600277, +0, PhaseType.AQUEOUS)
    KOH_aq = Species("KOH(aq)", None, ["K", "O", "H"], 0.05610564, +0, PhaseType.AQUEOUS)
    Kr_aq = Species("Kr(aq)", None, ["Kr"], 0.083798, +0, PhaseType.AQUEOUS)
    LiCl_aq = Species("LiCl(aq)", None, ["Li", "Cl"], 0.042394, +0, PhaseType.AQUEOUS)
    LiOH_aq = Species("LiOH(aq)", None, ["Li", "O", "H"], 0.023948340000000002, +0, PhaseType.AQUEOUS)
    MnO_aq = Species("MnO(aq)", None, ["Mn", "O"], 0.070937449, +0, PhaseType.AQUEOUS)
    MnSO4_aq = Species("MnSO4(aq)", None, ["Mn", "S", "O"], 0.15100064900000001, +0, PhaseType.AQUEOUS)
    N2_aq = Species("N2(aq)", None, ["N"], 0.0280134, +0, PhaseType.AQUEOUS)
    NH3_aq = Species("NH3(aq)", None, ["N", "H"], 0.01703052, +0, PhaseType.AQUEOUS)
    NaBr_aq = Species("NaBr(aq)", None, ["Na", "Br"], 0.10289377000000001, +0, PhaseType.AQUEOUS)
    NaCl_aq = Species("NaCl(aq)", None, ["Na", "Cl"], 0.058442770000000005, +0, PhaseType.AQUEOUS)
    NaF_aq = Species("NaF(aq)", None, ["Na", "F"], 0.0419881732, +0, PhaseType.AQUEOUS)
    NaHSiO3_aq = Species("NaHSiO3(aq)", None, ["Na", "H", "Si", "O"], 0.10008141000000001, +0, PhaseType.AQUEOUS)
    NaI_aq = Species("NaI(aq)", None, ["Na", "I"], 0.14989423999999998, +0, PhaseType.AQUEOUS)
    NaOH_aq = Species("NaOH(aq)", None, ["Na", "O", "H"], 0.03999711, +0, PhaseType.AQUEOUS)
    Ne_aq = Species("Ne(aq)", None, ["Ne"], 0.020179700000000002, +0, PhaseType.AQUEOUS)
    NiO_aq = Species("NiO(aq)", None, ["Ni", "O"], 0.0746928, +0, PhaseType.AQUEOUS)
    O2_aq = Species("O2(aq)", None, ["O"], 0.0319988, +0, PhaseType.AQUEOUS)
    PbCl2_aq = Species("PbCl2(aq)", None, ["Pb", "Cl"], 0.278106, +0, PhaseType.AQUEOUS)
    PbO_aq = Species("PbO(aq)", None, ["Pb", "O"], 0.2231994, +0, PhaseType.AQUEOUS)
    PdSO4_aq = Species("PdSO4(aq)", None, ["Pd", "S", "O"], 0.20248259999999998, +0, PhaseType.AQUEOUS)
    PdCl2_aq = Species("PdCl2(aq)", None, ["Pd", "Cl"], 0.17732599999999998, +0, PhaseType.AQUEOUS)
    PdO_aq = Species("PdO(aq)", None, ["Pd", "O"], 0.1224194, +0, PhaseType.AQUEOUS)
    PtSO4_aq = Species("PtSO4(aq)", None, ["Pt", "S", "O"], 0.2911406, +0, PhaseType.AQUEOUS)
    PtCl2_aq = Species("PtCl2(aq)", None, ["Pt", "Cl"], 0.265984, +0, PhaseType.AQUEOUS)
    PtO_aq = Species("PtO(aq)", None, ["Pt", "O"], 0.2110774, +0, PhaseType.AQUEOUS)
    RbBr_aq = Species("RbBr(aq)", None, ["Rb", "Br"], 0.1653718, +0, PhaseType.AQUEOUS)
    RbCl_aq = Species("RbCl(aq)", None, ["Rb", "Cl"], 0.1209208, +0, PhaseType.AQUEOUS)
    RbF_aq = Species("RbF(aq)", None, ["Rb", "F"], 0.1044662032, +0, PhaseType.AQUEOUS)
    RbI_aq = Species("RbI(aq)", None, ["Rb", "I"], 0.21237226999999997, +0, PhaseType.AQUEOUS)
    RbOH_aq = Species("RbOH(aq)", None, ["Rb", "O", "H"], 0.10247513999999999, +0, PhaseType.AQUEOUS)
    RhSO4_aq = Species("RhSO4(aq)", None, ["Rh", "S", "O"], 0.19896809999999998, +0, PhaseType.AQUEOUS)
    RhCl2_aq = Species("RhCl2(aq)", None, ["Rh", "Cl"], 0.1738115, +0, PhaseType.AQUEOUS)
    RhCl3_aq = Species("RhCl3(aq)", None, ["Rh", "Cl"], 0.2092645, +0, PhaseType.AQUEOUS)
    RhO_aq = Species("RhO(aq)", None, ["Rh", "O"], 0.1189049, +0, PhaseType.AQUEOUS)
    Rn_aq = Species("Rn(aq)", None, ["Rn"], 0.222, +0, PhaseType.AQUEOUS)
    RuSO4_aq = Species("RuSO4(aq)", None, ["Ru", "S", "O"], 0.1971326, +0, PhaseType.AQUEOUS)
    RuCl2_aq = Species("RuCl2(aq)", None, ["Ru", "Cl"], 0.171976, +0, PhaseType.AQUEOUS)
    RuCl3_aq = Species("RuCl3(aq)", None, ["Ru", "Cl"], 0.207429, +0, PhaseType.AQUEOUS)
    RuO_aq = Species("RuO(aq)", None, ["Ru", "O"], 0.1170694, +0, PhaseType.AQUEOUS)
    H2S2O3_aq = Species("H2S2O3(aq)", None, ["H", "S", "O"], 0.11414408000000001, +0, PhaseType.AQUEOUS)
    H2S2O4_aq = Species("H2S2O4(aq)", None, ["H", "S", "O"], 0.13014348, +0, PhaseType.AQUEOUS)
    SO2_aq = Species("SO2(aq)", None, ["S", "O"], 0.0640638, +0, PhaseType.AQUEOUS)
    HScO2_aq = Species("HScO2(aq)", None, ["H", "Sc", "O"], 0.07796265, +0, PhaseType.AQUEOUS)
    SiO2_aq = Species("SiO2(aq)", None, ["Si", "O"], 0.0600843, +0, PhaseType.AQUEOUS)
    SnO_aq = Species("SnO(aq)", None, ["Sn", "O"], 0.13470939999999998, +0, PhaseType.AQUEOUS)
    TlOH_aq = Species("TlOH(aq)", None, ["Tl", "O", "H"], 0.22139064, +0, PhaseType.AQUEOUS)
    HTlO2_aq = Species("HTlO2(aq)", None, ["H", "Tl", "O"], 0.23739004, +0, PhaseType.AQUEOUS)
    Xe_aq = Species("Xe(aq)", None, ["Xe"], 0.131293, +0, PhaseType.AQUEOUS)
    HYO2_aq = Species("HYO2(aq)", None, ["H", "Y", "O"], 0.12191259, +0, PhaseType.AQUEOUS)
    ZnCl2_aq = Species("ZnCl2(aq)", None, ["Zn", "Cl"], 0.136315, +0, PhaseType.AQUEOUS)
    ZnO_aq = Species("ZnO(aq)", None, ["Zn", "O"], 0.0814084, +0, PhaseType.AQUEOUS)
    HUO2_aq = Species("HUO2(aq)", None, ["U", "O", "H"], 0.27103564999999996, +0, PhaseType.AQUEOUS)
    UO2_aq = Species("UO2(aq)", None, ["U", "O"], 0.27002771000000003, +0, PhaseType.AQUEOUS)
    UO2OH_aq = Species("UO2OH(aq)", None, ["U", "O", "H"], 0.28703505, +0, PhaseType.AQUEOUS)
    UO3_aq = Species("UO3(aq)", None, ["U", "O"], 0.28602711, +0, PhaseType.AQUEOUS)
    HNO2_aq = Species("HNO2(aq)", None, ["H", "N", "O"], 0.047013440000000004, +0, PhaseType.AQUEOUS)
    H2N2O2_aq = Species("H2N2O2(aq)", None, ["H", "N", "O"], 0.06202808, +0, PhaseType.AQUEOUS)
    H3PO2_aq = Species("H3PO2(aq)", None, ["H", "P", "O"], 0.06599638099999999, +0, PhaseType.AQUEOUS)
    H3PO3_aq = Species("H3PO3(aq)", None, ["H", "P", "O"], 0.08199578099999999, +0, PhaseType.AQUEOUS)
    H4P2O7_aq = Species("H4P2O7(aq)", None, ["H", "P", "O"], 0.17797508199999998, +0, PhaseType.AQUEOUS)
    H3AsO4_aq = Species("H3AsO4(aq)", None, ["H", "As", "O"], 0.14194302, +0, PhaseType.AQUEOUS)
    HAsO2_aq = Species("HAsO2(aq)", None, ["H", "As", "O"], 0.10792834000000001, +0, PhaseType.AQUEOUS)
    HSbO2_aq = Species("HSbO2(aq)", None, ["H", "Sb", "O"], 0.15476673999999999, +0, PhaseType.AQUEOUS)
    HBiO2_aq = Species("HBiO2(aq)", None, ["H", "Bi", "O"], 0.24198712, +0, PhaseType.AQUEOUS)
    H2O2_aq = Species("H2O2(aq)", None, ["H", "O"], 0.03401468, +0, PhaseType.AQUEOUS)
    HClO2_aq = Species("HClO2(aq)", None, ["H", "Cl", "O"], 0.06845973999999999, +0, PhaseType.AQUEOUS)
    HIO3_aq = Species("HIO3(aq)", None, ["H", "I", "O"], 0.17591061, +0, PhaseType.AQUEOUS)
    HCrO2_aq = Species("HCrO2(aq)", None, ["H", "Cr", "O"], 0.08500284000000001, +0, PhaseType.AQUEOUS)
    ZrO2_aq = Species("ZrO2(aq)", None, ["Zr", "O"], 0.12322280000000001, +0, PhaseType.AQUEOUS)
    HNbO3_aq = Species("HNbO3(aq)", None, ["H", "Nb", "O"], 0.14191252000000001, +0, PhaseType.AQUEOUS)
    HfO2_aq = Species("HfO2(aq)", None, ["Hf", "O"], 0.2104888, +0, PhaseType.AQUEOUS)
    LaO2H_aq = Species("LaO2H(aq)", None, ["La", "O", "H"], 0.17191224, +0, PhaseType.AQUEOUS)
    LaCl3_aq = Species("LaCl3(aq)", None, ["La", "Cl"], 0.2452645, +0, PhaseType.AQUEOUS)
    LaF3_aq = Species("LaF3(aq)", None, ["La", "F"], 0.1959007096, +0, PhaseType.AQUEOUS)
    CeO2H_aq = Species("CeO2H(aq)", None, ["Ce", "O", "H"], 0.17312274, +0, PhaseType.AQUEOUS)
    CeCl3_aq = Species("CeCl3(aq)", None, ["Ce", "Cl"], 0.246475, +0, PhaseType.AQUEOUS)
    CeF3_aq = Species("CeF3(aq)", None, ["Ce", "F"], 0.1971112096, +0, PhaseType.AQUEOUS)
    PrCl3_aq = Species("PrCl3(aq)", None, ["Pr", "Cl"], 0.24726665, +0, PhaseType.AQUEOUS)
    PrF3_aq = Species("PrF3(aq)", None, ["Pr", "F"], 0.1979028596, +0, PhaseType.AQUEOUS)
    PrO2H_aq = Species("PrO2H(aq)", None, ["Pr", "O", "H"], 0.17391439, +0, PhaseType.AQUEOUS)
    NdO2H_aq = Species("NdO2H(aq)", None, ["Nd", "O", "H"], 0.17724673999999999, +0, PhaseType.AQUEOUS)
    NdCl3_aq = Species("NdCl3(aq)", None, ["Nd", "Cl"], 0.250599, +0, PhaseType.AQUEOUS)
    NdF3_aq = Species("NdF3(aq)", None, ["Nd", "F"], 0.2012352096, +0, PhaseType.AQUEOUS)
    SmO2H_aq = Species("SmO2H(aq)", None, ["Sm", "O", "H"], 0.18336674, +0, PhaseType.AQUEOUS)
    SmCl3_aq = Species("SmCl3(aq)", None, ["Sm", "Cl"], 0.256719, +0, PhaseType.AQUEOUS)
    SmF3_aq = Species("SmF3(aq)", None, ["Sm", "F"], 0.2073552096, +0, PhaseType.AQUEOUS)
    EuO2H_aq = Species("EuO2H(aq)", None, ["Eu", "O", "H"], 0.18497074, +0, PhaseType.AQUEOUS)
    EuCl3_aq = Species("EuCl3(aq)", None, ["Eu", "Cl"], 0.25832299999999997, +0, PhaseType.AQUEOUS)
    EuF2_aq = Species("EuF2(aq)", None, ["Eu", "F"], 0.1709624032, +0, PhaseType.AQUEOUS)
    EuCl2_aq = Species("EuCl2(aq)", None, ["Eu", "Cl"], 0.22287, +0, PhaseType.AQUEOUS)
    EuF3_aq = Species("EuF3(aq)", None, ["Eu", "F"], 0.2089592096, +0, PhaseType.AQUEOUS)
    GdO2H_aq = Species("GdO2H(aq)", None, ["Gd", "O", "H"], 0.19025674, +0, PhaseType.AQUEOUS)
    GdCl3_aq = Species("GdCl3(aq)", None, ["Gd", "Cl"], 0.263609, +0, PhaseType.AQUEOUS)
    GdF3_aq = Species("GdF3(aq)", None, ["Gd", "F"], 0.21424520960000001, +0, PhaseType.AQUEOUS)
    TbO2H_aq = Species("TbO2H(aq)", None, ["Tb", "O", "H"], 0.19193208, +0, PhaseType.AQUEOUS)
    TbCl3_aq = Species("TbCl3(aq)", None, ["Tb", "Cl"], 0.26528434, +0, PhaseType.AQUEOUS)
    TbF3_aq = Species("TbF3(aq)", None, ["Tb", "F"], 0.21592054959999998, +0, PhaseType.AQUEOUS)
    DyCl3_aq = Species("DyCl3(aq)", None, ["Dy", "Cl"], 0.26885899999999996, +0, PhaseType.AQUEOUS)
    DyF3_aq = Species("DyF3(aq)", None, ["Dy", "F"], 0.21949520960000002, +0, PhaseType.AQUEOUS)
    DyO2H_aq = Species("DyO2H(aq)", None, ["Dy", "O", "H"], 0.19550674, +0, PhaseType.AQUEOUS)
    HoCl3_aq = Species("HoCl3(aq)", None, ["Ho", "Cl"], 0.27128932, +0, PhaseType.AQUEOUS)
    HoF3_aq = Species("HoF3(aq)", None, ["Ho", "F"], 0.2219255296, +0, PhaseType.AQUEOUS)
    HoO2H_aq = Species("HoO2H(aq)", None, ["Ho", "O", "H"], 0.19793706, +0, PhaseType.AQUEOUS)
    ErCl3_aq = Species("ErCl3(aq)", None, ["Er", "Cl"], 0.273618, +0, PhaseType.AQUEOUS)
    ErF3_aq = Species("ErF3(aq)", None, ["Er", "F"], 0.2242542096, +0, PhaseType.AQUEOUS)
    ErO2H_aq = Species("ErO2H(aq)", None, ["Er", "O", "H"], 0.20026574, +0, PhaseType.AQUEOUS)
    TmCl3_aq = Species("TmCl3(aq)", None, ["Tm", "Cl"], 0.27529321, +0, PhaseType.AQUEOUS)
    TmF3_aq = Species("TmF3(aq)", None, ["Tm", "F"], 0.2259294196, +0, PhaseType.AQUEOUS)
    TmO2H_aq = Species("TmO2H(aq)", None, ["Tm", "O", "H"], 0.20194094999999998, +0, PhaseType.AQUEOUS)
    YbO2H_aq = Species("YbO2H(aq)", None, ["Yb", "O", "H"], 0.20604674, +0, PhaseType.AQUEOUS)
    YbCl3_aq = Species("YbCl3(aq)", None, ["Yb", "Cl"], 0.279399, +0, PhaseType.AQUEOUS)
    YbF3_aq = Species("YbF3(aq)", None, ["Yb", "F"], 0.2300352096, +0, PhaseType.AQUEOUS)
    LuO2H_aq = Species("LuO2H(aq)", None, ["Lu", "O", "H"], 0.20797374, +0, PhaseType.AQUEOUS)
    LuCl3_aq = Species("LuCl3(aq)", None, ["Lu", "Cl"], 0.281326, +0, PhaseType.AQUEOUS)
    LuF3_aq = Species("LuF3(aq)", None, ["Lu", "F"], 0.2319622096, +0, PhaseType.AQUEOUS)
    MgSO4_aq = Species("MgSO4(aq)", None, ["Mg", "S", "O"], 0.12036759999999999, +0, PhaseType.AQUEOUS)
    HCl_aq = Species("HCl(aq)", None, ["H", "Cl"], 0.036460940000000004, +0, PhaseType.AQUEOUS)
    MgCO3_aq = Species("MgCO3(aq)", None, ["Mg", "C", "O"], 0.0843139, +0, PhaseType.AQUEOUS)
    CaCO3_aq = Species("CaCO3(aq)", None, ["Ca", "C", "O"], 0.1000869, +0, PhaseType.AQUEOUS)
    SrCO3_aq = Species("SrCO3(aq)", None, ["Sr", "C", "O"], 0.14762889999999998, +0, PhaseType.AQUEOUS)
    BaCO3_aq = Species("BaCO3(aq)", None, ["Ba", "C", "O"], 0.1973359, +0, PhaseType.AQUEOUS)
    BeCl2_aq = Species("BeCl2(aq)", None, ["Be", "Cl"], 0.079918182, +0, PhaseType.AQUEOUS)
    CuCl_aq = Species("CuCl(aq)", None, ["Cu", "Cl"], 0.09899899999999999, +0, PhaseType.AQUEOUS)
    CuCl2_aq = Species("CuCl2(aq)", None, ["Cu", "Cl"], 0.134452, +0, PhaseType.AQUEOUS)
    CdCl2_aq = Species("CdCl2(aq)", None, ["Cd", "Cl"], 0.183317, +0, PhaseType.AQUEOUS)
    TlCl_aq = Species("TlCl(aq)", None, ["Tl", "Cl"], 0.2398363, +0, PhaseType.AQUEOUS)
    AuCl_aq = Species("AuCl(aq)", None, ["Au", "Cl"], 0.23241954999999997, +0, PhaseType.AQUEOUS)
    HgCl2_aq = Species("HgCl2(aq)", None, ["Hg", "Cl"], 0.27149599999999996, +0, PhaseType.AQUEOUS)
    BeF2_aq = Species("BeF2(aq)", None, ["Be", "F"], 0.0470089884, +0, PhaseType.AQUEOUS)
    AgF_aq = Species("AgF(aq)", None, ["Ag", "F"], 0.1268666032, +0, PhaseType.AQUEOUS)
    CdF2_aq = Species("CdF2(aq)", None, ["Cd", "F"], 0.1504078064, +0, PhaseType.AQUEOUS)
    TlF_aq = Species("TlF(aq)", None, ["Tl", "F"], 0.2233817032, +0, PhaseType.AQUEOUS)
    PbF2_aq = Species("PbF2(aq)", None, ["Pb", "F"], 0.24519680640000002, +0, PhaseType.AQUEOUS)
    Pb_HS_2_aq = Species("Pb(HS2(aq)", None, ["Pb", "H", "S"], 0.27334588000000004, +0, PhaseType.AQUEOUS)

    # reaktoro liquid species
    H2O_l = Species("H2O(l", None, ["H", "O"], 0.0180153, +0, PhaseType.LIQUID)

    # reaktoro elements
    H = Species("H", None, ["H"], 0.001007940, +0, PhaseType.ELEMENT)
    He = Species("He", None, ["He"], 0.004002602, +0, PhaseType.ELEMENT)
    Li = Species("Li", None, ["Li"], 0.006941000, +0, PhaseType.ELEMENT)
    Be = Species("Be", None, ["Be"], 0.009012182, +0, PhaseType.ELEMENT)
    B = Species("B", None, ["B"], 0.010811000, +0, PhaseType.ELEMENT)
    C = Species("C", None, ["C"], 0.012010700, +0, PhaseType.ELEMENT)
    N = Species("N", None, ["N"], 0.014006700, +0, PhaseType.ELEMENT)
    O = Species("O", None, ["O"], 0.015999400, +0, PhaseType.ELEMENT)
    F = Species("F", None, ["F"], 0.018998403, +0, PhaseType.ELEMENT)
    Ne = Species("Ne", None, ["Ne"], 0.020179700, +0, PhaseType.ELEMENT)
    Na = Species("Na", None, ["Na"], 0.022989770, +0, PhaseType.ELEMENT)
    Mg = Species("Mg", None, ["Mg"], 0.024305000, +0, PhaseType.ELEMENT)
    Al = Species("Al", None, ["Al"], 0.026981538, +0, PhaseType.ELEMENT)
    Si = Species("Si", None, ["Si"], 0.028085500, +0, PhaseType.ELEMENT)
    P = Species("P", None, ["P"], 0.030973761, +0, PhaseType.ELEMENT)
    S = Species("S", None, ["S"], 0.032065000, +0, PhaseType.ELEMENT)
    Cl = Species("Cl", None, ["Cl"], 0.035453000, +0, PhaseType.ELEMENT)
    K = Species("K", None, ["K"], 0.039098300, +0, PhaseType.ELEMENT)
    Ar = Species("Ar", None, ["Ar"], 0.039948000, +0, PhaseType.ELEMENT)
    Ca = Species("Ca", None, ["Ca"], 0.040078000, +0, PhaseType.ELEMENT)
    Sc = Species("Sc", None, ["Sc"], 0.044955910, +0, PhaseType.ELEMENT)
    Ti = Species("Ti", None, ["Ti"], 0.047867000, +0, PhaseType.ELEMENT)
    V = Species("V", None, ["V"], 0.050941500, +0, PhaseType.ELEMENT)
    Cr = Species("Cr", None, ["Cr"], 0.051996100, +0, PhaseType.ELEMENT)
    Mn = Species("Mn", None, ["Mn"], 0.054938050, +0, PhaseType.ELEMENT)
    Fe = Species("Fe", None, ["Fe"], 0.055845000, +0, PhaseType.ELEMENT)
    Ni = Species("Ni", None, ["Ni"], 0.058693400, +0, PhaseType.ELEMENT)
    Co = Species("Co", None, ["Co"], 0.058933200, +0, PhaseType.ELEMENT)
    Cu = Species("Cu", None, ["Cu"], 0.063546000, +0, PhaseType.ELEMENT)
    Zn = Species("Zn", None, ["Zn"], 0.065409000, +0, PhaseType.ELEMENT)
    Ga = Species("Ga", None, ["Ga"], 0.069723000, +0, PhaseType.ELEMENT)
    Ge = Species("Ge", None, ["Ge"], 0.072640000, +0, PhaseType.ELEMENT)
    As = Species("As", None, ["As"], 0.074921600, +0, PhaseType.ELEMENT)
    Se = Species("Se", None, ["Se"], 0.078960000, +0, PhaseType.ELEMENT)
    Br = Species("Br", None, ["Br"], 0.079904000, +0, PhaseType.ELEMENT)
    Kr = Species("Kr", None, ["Kr"], 0.083798000, +0, PhaseType.ELEMENT)
    Rb = Species("Rb", None, ["Rb"], 0.085467800, +0, PhaseType.ELEMENT)
    Sr = Species("Sr", None, ["Sr"], 0.087620000, +0, PhaseType.ELEMENT)
    Y = Species("Y", None, ["Y"], 0.088905850, +0, PhaseType.ELEMENT)
    Zr = Species("Zr", None, ["Zr"], 0.091224000, +0, PhaseType.ELEMENT)
    Nb = Species("Nb", None, ["Nb"], 0.092906380, +0, PhaseType.ELEMENT)
    Mo = Species("Mo", None, ["Mo"], 0.095940000, +0, PhaseType.ELEMENT)
    Tc = Species("Tc", None, ["Tc"], 0.098000000, +0, PhaseType.ELEMENT)
    Ru = Species("Ru", None, ["Ru"], 0.101070000, +0, PhaseType.ELEMENT)
    Rh = Species("Rh", None, ["Rh"], 0.102905500, +0, PhaseType.ELEMENT)
    Pd = Species("Pd", None, ["Pd"], 0.106420000, +0, PhaseType.ELEMENT)
    Ag = Species("Ag", None, ["Ag"], 0.107868200, +0, PhaseType.ELEMENT)
    Cd = Species("Cd", None, ["Cd"], 0.112411000, +0, PhaseType.ELEMENT)
    In = Species("In", None, ["In"], 0.114818000, +0, PhaseType.ELEMENT)
    Sn = Species("Sn", None, ["Sn"], 0.118710000, +0, PhaseType.ELEMENT)
    Sb = Species("Sb", None, ["Sb"], 0.121760000, +0, PhaseType.ELEMENT)
    I = Species("I", None, ["I"], 0.126904470, +0, PhaseType.ELEMENT)
    Te = Species("Te", None, ["Te"], 0.127600000, +0, PhaseType.ELEMENT)
    Xe = Species("Xe", None, ["Xe"], 0.131293000, +0, PhaseType.ELEMENT)
    Cs = Species("Cs", None, ["Cs"], 0.132905450, +0, PhaseType.ELEMENT)
    Ba = Species("Ba", None, ["Ba"], 0.137327000, +0, PhaseType.ELEMENT)
    La = Species("La", None, ["La"], 0.138905500, +0, PhaseType.ELEMENT)
    Ce = Species("Ce", None, ["Ce"], 0.140116000, +0, PhaseType.ELEMENT)
    Pr = Species("Pr", None, ["Pr"], 0.140907650, +0, PhaseType.ELEMENT)
    Nd = Species("Nd", None, ["Nd"], 0.144240000, +0, PhaseType.ELEMENT)
    Pm = Species("Pm", None, ["Pm"], 0.145000000, +0, PhaseType.ELEMENT)
    Sm = Species("Sm", None, ["Sm"], 0.150360000, +0, PhaseType.ELEMENT)
    Eu = Species("Eu", None, ["Eu"], 0.151964000, +0, PhaseType.ELEMENT)
    Gd = Species("Gd", None, ["Gd"], 0.157250000, +0, PhaseType.ELEMENT)
    Tb = Species("Tb", None, ["Tb"], 0.158925340, +0, PhaseType.ELEMENT)
    Dy = Species("Dy", None, ["Dy"], 0.162500000, +0, PhaseType.ELEMENT)
    Ho = Species("Ho", None, ["Ho"], 0.164930320, +0, PhaseType.ELEMENT)
    Er = Species("Er", None, ["Er"], 0.167259000, +0, PhaseType.ELEMENT)
    Tm = Species("Tm", None, ["Tm"], 0.168934210, +0, PhaseType.ELEMENT)
    Yb = Species("Yb", None, ["Yb"], 0.173040000, +0, PhaseType.ELEMENT)
    Lu = Species("Lu", None, ["Lu"], 0.174967000, +0, PhaseType.ELEMENT)
    Hf = Species("Hf", None, ["Hf"], 0.178490000, +0, PhaseType.ELEMENT)
    Ta = Species("Ta", None, ["Ta"], 0.180947900, +0, PhaseType.ELEMENT)
    W = Species("W", None, ["W"], 0.183840000, +0, PhaseType.ELEMENT)
    Re = Species("Re", None, ["Re"], 0.186207000, +0, PhaseType.ELEMENT)
    Os = Species("Os", None, ["Os"], 0.190230000, +0, PhaseType.ELEMENT)
    Ir = Species("Ir", None, ["Ir"], 0.192217000, +0, PhaseType.ELEMENT)
    Pt = Species("Pt", None, ["Pt"], 0.195078000, +0, PhaseType.ELEMENT)
    Au = Species("Au", None, ["Au"], 0.196966550, +0, PhaseType.ELEMENT)
    Hg = Species("Hg", None, ["Hg"], 0.200590000, +0, PhaseType.ELEMENT)
    Tl = Species("Tl", None, ["Tl"], 0.204383300, +0, PhaseType.ELEMENT)
    Pb = Species("Pb", None, ["Pb"], 0.207200000, +0, PhaseType.ELEMENT)
    Bi = Species("Bi", None, ["Bi"], 0.208980380, +0, PhaseType.ELEMENT)
    Po = Species("Po", None, ["Po"], 0.209000000, +0, PhaseType.ELEMENT)
    At = Species("At", None, ["At"], 0.210000000, +0, PhaseType.ELEMENT)
    Rn = Species("Rn", None, ["Rn"], 0.222000000, +0, PhaseType.ELEMENT)
    Fr = Species("Fr", None, ["Fr"], 0.223000000, +0, PhaseType.ELEMENT)
    Ra = Species("Ra", None, ["Ra"], 0.226000000, +0, PhaseType.ELEMENT)
    Ac = Species("Ac", None, ["Ac"], 0.227000000, +0, PhaseType.ELEMENT)
    Pa = Species("Pa", None, ["Pa"], 0.231035880, +0, PhaseType.ELEMENT)
    Th = Species("Th", None, ["Th"], 0.232038100, +0, PhaseType.ELEMENT)
    Np = Species("Np", None, ["Np"], 0.237000000, +0, PhaseType.ELEMENT)
    U = Species("U", None, ["U"], 0.238028910, +0, PhaseType.ELEMENT)
    Am = Species("Am", None, ["Am"], 0.243000000, +0, PhaseType.ELEMENT)
    Pu = Species("Pu", None, ["Pu"], 0.244000000, +0, PhaseType.ELEMENT)
    Bk = Species("Bk", None, ["Bk"], 0.247000000, +0, PhaseType.ELEMENT)
    Cm = Species("Cm", None, ["Cm"], 0.247000000, +0, PhaseType.ELEMENT)
    Cf = Species("Cf", None, ["Cf"], 0.251000000, +0, PhaseType.ELEMENT)
    Es = Species("Es", None, ["Es"], 0.252000000, +0, PhaseType.ELEMENT)
    Fm = Species("Fm", None, ["Fm"], 0.257000000, +0, PhaseType.ELEMENT)
    Md = Species("Md", None, ["Md"], 0.258000000, +0, PhaseType.ELEMENT)
    No = Species("No", None, ["No"], 0.259000000, +0, PhaseType.ELEMENT)
    Rf = Species("Rf", None, ["Rf"], 0.261000000, +0, PhaseType.ELEMENT)
    Lr = Species("Lr", None, ["Lr"], 0.262000000, +0, PhaseType.ELEMENT)


class LookUp:

    reaktoroToComp = {
        "H2O(g)": Comp.STEAM,
        "H2O(aq)": Comp.WATER,
        "H2(g)": Comp.H2_g,
        "O2(g)": Comp.O2_g,
        "NH3": Comp.AMMONIA,
        "NH3(g)": Comp.AMMONIA_g,
        "CO2(g)": Comp.CARBONDIOXIDE,
        "N2(g)": Comp.NITROGEN,
        "H2S(g)": Comp.H2S,
        "He(g)": Comp.He_g,
        "Ar(g)": Comp.ARGON,
        "CH4(g)": Comp.METHANE,
        "CO(g)": Comp.CO_g,
        "C2H4(g)": Comp.C2H4_g,
        "S2(g)": Comp.S2_g,
        "SO2(g)": Comp.SO2_g,
        "Kr(g)": Comp.Kr_g,
        "Ne(g)": Comp.Ne_g,
        "Rn(g)": Comp.Rn_g,
        "Xe(g)": Comp.Xe_g,
        "Ag(CO3)-": Comp.Ag_CO3_minus,
        "Ag(CO3)2---": Comp.Ag_CO3_2_minus3,
        "Ag+": Comp.Ag_plus,
        "Ag++": Comp.Ag_plus2,
        "AgCl2-": Comp.AgCl2_minus,
        "AgCl3--": Comp.AgCl3_minus2,
        "AgCl4---": Comp.AgCl4_minus3,
        "AgO-": Comp.AgO_minus,
        "Al+++": Comp.Al_plus3,
        "AlO+": Comp.AlO_plus,
        "AlOH++": Comp.AlOH_plus2,
        "AlO2-": Comp.AlO2_minus,
        "Au+": Comp.Au_plus,
        "Au+++": Comp.Au_plus3,
        "BF4-": Comp.BF4_minus,
        "BO2-": Comp.BO2_minus,
        "Ba(HCO3)+": Comp.Ba_HCO3_plus,
        "Ba++": Comp.Ba_plus2,
        "BaCl+": Comp.BaCl_plus,
        "BaOH+": Comp.BaOH_plus,
        "Be++": Comp.Be_plus2,
        "BeOH+": Comp.BeOH_plus,
        "HBeO2-": Comp.HBeO2_minus,
        "BeO2--": Comp.BeO2_minus2,
        "Br-": Comp.Br_minus,
        "Br3-": Comp.Br3_minus,
        "BrO-": Comp.BrO_minus,
        "BrO3-": Comp.BrO3_minus,
        "BrO4-": Comp.BrO4_minus,
        "CaOH+": Comp.CaOH_plus,
        "Ce++++": Comp.Ce_plus4,
        "CN-": Comp.CN_minus,
        "CO3--": Comp.CO3_minus2,
        "Ca(HCO3)+": Comp.Ca_HCO3_plus,
        "Ca++": Comp.Ca_plus2,
        "CaCl+": Comp.CaCl_plus,
        "CaF+": Comp.CaF_plus,
        "Cd++": Comp.Cd_plus2,
        "CdOH+": Comp.CdOH_plus,
        "HCdO2-": Comp.HCdO2_minus,
        "CdO2--": Comp.CdO2_minus2,
        "Ce++": Comp.Ce_plus2,
        "Ce+++": Comp.Ce_plus3,
        "Cl-": Comp.Cl_minus,
        "ClO-": Comp.ClO_minus,
        "ClO2-": Comp.ClO2_minus,
        "ClO3-": Comp.ClO3_minus,
        "ClO4-": Comp.ClO4_minus,
        "Co++": Comp.Co_plus2,
        "Co+++": Comp.Co_plus3,
        "CoOH+": Comp.CoOH_plus,
        "HCoO2-": Comp.HCoO2_minus,
        "CoO2--": Comp.CoO2_minus2,
        "CoOH++": Comp.CoOH_plus2,
        "Cr2O7--": Comp.Cr2O7_minus2,
        "CrO4--": Comp.CrO4_minus2,
        "Cs+": Comp.Cs_plus,
        "Cu+": Comp.Cu_plus,
        "Cu++": Comp.Cu_plus2,
        "CuOH+": Comp.CuOH_plus,
        "HCuO2-": Comp.HCuO2_minus,
        "CuO2--": Comp.CuO2_minus2,
        "Dy++": Comp.Dy_plus2,
        "Dy+++": Comp.Dy_plus3,
        "Dy++++": Comp.Dy_plus4,
        "Er++": Comp.Er_plus2,
        "Er+++": Comp.Er_plus3,
        "Er++++": Comp.Er_plus4,
        "Eu++": Comp.Eu_plus2,
        "Eu+++": Comp.Eu_plus3,
        "Eu++++": Comp.Eu_plus4,
        "F-": Comp.F_minus,
        "Fe++": Comp.Fe_plus2,
        "Fe+++": Comp.Fe_plus3,
        "FeCl+": Comp.FeCl_plus,
        "FeOH++": Comp.FeOH_plus2,
        "FeOH+": Comp.FeOH_plus,
        "FeO+": Comp.FeO_plus,
        "HFeO2-": Comp.HFe2O_minus,
        "FeO2-": Comp.FeO2_minus,
        "Ga+++": Comp.Ga_plus3,
        "GaOH++": Comp.GaOH_plus2,
        "GaO+": Comp.GaO_plus,
        "GaO2-": Comp.GaO2_minus,
        "Gd++": Comp.Gd_plus2,
        "Gd+++": Comp.Gd_plus3,
        "Gd++++": Comp.Gd_plus4,
        "H+": Comp.H_plus,
        "H2AsO3-": Comp.H2AsO3_minus,
        "H2AsO4-": Comp.H2AsO4_minus,
        "H2P2O7--": Comp.H2P2O7_minus2,
        "H2PO4-": Comp.H2PO4_minus,
        "H2VO4-": Comp.H2VO4_minus,
        "H3P2O7-": Comp.H3P2O7_minus,
        "HAsO4--": Comp.HAsO4_minus2,
        "HCO3-": Comp.HCO3_minus,
        "HCrO4-": Comp.HCrO4_minus,
        "HF2-": Comp.HF2_minus,
        "HO2-": Comp.HO2_minus,
        "HPO4--": Comp.HPO4_minus2,
        "HS-": Comp.HS_minus,
        "HSO3-": Comp.HSO3_minus,
        "HSO4-": Comp.HSO4_minus,
        "HSO5-": Comp.HSO5_minus,
        "HSe-": Comp.HSe_minus,
        "HSeO3-": Comp.HSeO3_minus,
        "HSeO4-": Comp.HSeO4_minus,
        "HSiO3-": Comp.HSiO3_minus,
        "HVO4--": Comp.HVO4_minus2,
        "Hg++": Comp.Hg_plus2,
        "HgOH+": Comp.HgOH_plus,
        "HHgO2-": Comp.HHgO2_minus,
        "Hg2++": Comp.Hg2_plus2,
        "Ho++": Comp.Ho_plus2,
        "Ho+++": Comp.Ho_plus3,
        "Ho++++": Comp.Ho_plus4,
        "I-": Comp.I_minus,
        "I3-": Comp.I3_minus,
        "IO-": Comp.IO_minus,
        "IO3-": Comp.IO3_minus,
        "IO4-": Comp.IO4_minus,
        "In+++": Comp.In_plus3,
        "InOH++": Comp.InOH_plus2,
        "InO+": Comp.InO_plus,
        "InO2-": Comp.InO2_minus,
        "K+": Comp.K_plus,
        "KSO4-": Comp.KSO4_minus,
        "La+++": Comp.La_plus3,
        "Li+": Comp.Li_plus,
        "Lu+++": Comp.Lu_plus3,
        "Lu++++": Comp.Lu_plus4,
        "Mg(HCO3)+": Comp.Mg_HCO3_plus,
        "Mg++": Comp.Mg_plus2,
        "MgCl+": Comp.MgCl_plus,
        "MgF+": Comp.MgF_plus,
        "MgOH+": Comp.MgOH_plus,
        "Mn++": Comp.Mn_plus2,
        "Mn+++": Comp.Mn_plus3,
        "MnCl+": Comp.MnCl_plus,
        "MnOH+": Comp.MnOH_plus,
        "HMnO2-": Comp.HMnO2_minus,
        "MnO2--": Comp.MnO2_minus2,
        "MnO4-": Comp.MnO4_minus,
        "MnO4--": Comp.MnO4_minus2,
        "HMoO4-": Comp.HMoO4_minus,
        "MoO4--": Comp.MoO4_minus2,
        "NH4+": Comp.NH4_plus,
        "NO2-": Comp.NO2_minus,
        "NO3-": Comp.NO3_minus,
        "Na+": Comp.Na_plus,
        "Nd++": Comp.Nd_plus2,
        "Nd+++": Comp.Nd_plus3,
        "Nd++++": Comp.Nd_plus4,
        "Ni++": Comp.Ni_plus2,
        "NiCl+": Comp.NiCl_plus,
        "NiOH+": Comp.NiOH_plus,
        "HNiO2-": Comp.HNiO2_minus,
        "NiO2--": Comp.NiO2_minus2,
        "OH-": Comp.OH_minus,
        "PO4---": Comp.PO4_minus3,
        "Pb++": Comp.Pb_plus2,
        "PbCl+": Comp.PbCl_plus,
        "PbCl3-": Comp.PbCl3_minus,
        "PbCl4--": Comp.PbCl4_minus2,
        "PbOH+": Comp.PbOH_plus,
        "HPbO2-": Comp.HPbO2_minus,
        "PdOH+": Comp.Pd_OH_plus,
        "Pd(SO4)2--": Comp.Pd_SO4_2_minus_plus2,
        "Pd(SO4)3----": Comp.Pd_SO4_3_minus4,
        "Pd++": Comp.Pd_plus2,
        "PdCl+": Comp.PdCl_plus,
        "PdCl3-": Comp.PdCl3_minus,
        "PdCl4--": Comp.PdCl4_minus2,
        "Pr++": Comp.Pr_plus2,
        "Pr+++": Comp.Pr_plus3,
        "Pr++++": Comp.Pr_plus4,
        "PtOH+": Comp.Pt_OH_plus,
        "Pt(SO4)2--": Comp.Pt_SO4_2_minus2,
        "Pt(SO4)3----": Comp.Pt_SO4_3_minus4,
        "Pt++": Comp.Pt_plus2,
        "PtCl+": Comp.PtCl_plus,
        "PtCl3-": Comp.PtCl3_minus,
        "PtCl4--": Comp.PtCl4_minus2,
        "Ra++": Comp.Ra_plus2,
        "Rb+": Comp.Rb_plus,
        "ReO4-": Comp.ReO4_minus,
        "RhOH+": Comp.Rh_OH_plus,
        "RhOH++": Comp.Rh_OH_plus2,
        "RhSO4+": Comp.Rh_SO4_plus,
        "Rh(SO4)2-": Comp.Rh_SO4_2_minus,
        "Rh(SO4)2--": Comp.Rh_SO4_2_minus2,
        "Rh(SO4)3---": Comp.Rh_SO4_3_minus3,
        "Rh(SO4)3----": Comp.Rh_SO4_3_minus4,
        "Rh++": Comp.Rh_plus2,
        "Rh+++": Comp.Rh_plus3,
        "RhCl+": Comp.RhCl_plus,
        "RhCl++": Comp.RhCl_plus2,
        "RhCl2+": Comp.RhCl2_plus,
        "RhCl3-": Comp.RhCl3_minus,
        "RhCl4-": Comp.RhCl4_minus,
        "RhCl4--": Comp.RhCl4_minus2,
        "RhO+": Comp.RhO_plus,
        "RuOH+": Comp.Ru_OH_plus,
        "RuOH++": Comp.Ru_OH_plus2,
        "RuO4--": Comp.RuO4_minus2,
        "RuSO4+": Comp.Ru_SO4_plus,
        "Ru(SO4)2-": Comp.Ru_SO4_2_minus,
        "Ru(SO4)2--": Comp.Ru_SO4_2_minus2,
        "Ru(SO4)3---": Comp.Ru_SO4_3_minus3,
        "Ru(SO4)3----": Comp.Ru_SO4_3_minus4,
        "Ru++": Comp.Ru_plus2,
        "Ru+++": Comp.Ru_plus3,
        "RuCl+": Comp.RuCl_plus,
        "RuCl++": Comp.RuCl_plus2,
        "RuCl2+": Comp.RuCl2_plus,
        "RuCl3-": Comp.RuCl3_minus,
        "RuCl4-": Comp.RuCl4_minus,
        "RuCl4--": Comp.RuCl4_minus2,
        "RuCl5--": Comp.Ru_plusCl_5_minus_plus2,
        "RuCl6---": Comp.RuCl6_minus3,
        "RuO+": Comp.RuO_plus,
        "S2--": Comp.S2_minus2,
        "S2O3--": Comp.S2O3_minus2,
        "HS2O3-": Comp.HS2O3_minus,
        "S2O4--": Comp.S2O4_minus2,
        "HS2O4-": Comp.HS2O4_minus,
        "S2O5--": Comp.S2O5_minus2,
        "S2O6--": Comp.S2O6_minus2,
        "S2O8--": Comp.S2O8_minus2,
        "S3--": Comp.S3_minus2,
        "S3O6--": Comp.S3O6_minus2,
        "S4--": Comp.S4_minus2,
        "S4O6--": Comp.S4O6_minus2,
        "S5--": Comp.S5_minus2,
        "S5O6--": Comp.S5O6_minus2,
        "SO3--": Comp.SO3_minus2,
        "SO4--": Comp.SO4_minus2,
        "Sc+++": Comp.Sc_plus3,
        "ScOH++": Comp.ScOH_plus2,
        "ScO+": Comp.ScO_plus,
        "ScO2-": Comp.ScO2_minus,
        "SeO3--": Comp.SeO3_minus2,
        "SeO4--": Comp.SeO4_minus2,
        "SiF6--": Comp.SiF6_minus2,
        "Sm++": Comp.Sm_plus2,
        "Sm+++": Comp.Sm_plus3,
        "Sm++++": Comp.Sm_plus4,
        "Sn++": Comp.Sn_plus2,
        "SnOH+": Comp.SnOH_plus,
        "HSnO2-": Comp.HSnO2_minus,
        "Sr(HCO3)+": Comp.Sr_HCO3_plus,
        "Sr++": Comp.Sr_plus2,
        "SrCl+": Comp.SrCl_plus,
        "SrF+": Comp.SrF_plus,
        "SrOH+": Comp.SrOH_plus,
        "Tb++": Comp.Tb_plus2,
        "Tb+++": Comp.Tb_plus3,
        "Tb++++": Comp.Tb_plus4,
        "Th++++": Comp.Th_plus4,
        "Tl+": Comp.Tl_plus,
        "Tl+++": Comp.Tl_plus3,
        "TlOH++": Comp.TlOH_plus2,
        "TlO+": Comp.TlO_plus,
        "TlO2-": Comp.TlO2_minus,
        "Tm++": Comp.Tm_plus2,
        "Tm+++": Comp.Tm_plus3,
        "Tm++++": Comp.Tm_plus4,
        "U+++": Comp.U_plus3,
        "U++++": Comp.U_plus4,
        "UO2+": Comp.UO2_plus,
        "UO2++": Comp.UO2_plus2,
        "VO+": Comp.VO_plus,
        "VO++": Comp.VO_plus2,
        "VOH+": Comp.VOH_plus,
        "VOH++": Comp.VOH_plus2,
        "VO2+": Comp.VO2_plus,
        "VOOH+": Comp.VOOH_plus,
        "WO4--": Comp.WO4_minus2,
        "HWO4-": Comp.HWO4_minus,
        "Y+++": Comp.Y_plus3,
        "YOH++": Comp.YOH_plus2,
        "YO+": Comp.YO_plus,
        "YO2-": Comp.YO2_minus,
        "Yb++": Comp.Yb_plus2,
        "Yb+++": Comp.Yb_plus3,
        "Yb++++": Comp.Yb_plus4,
        "Zn++": Comp.Zn_plus2,
        "ZnCl+": Comp.ZnCl_plus,
        "ZnCl3-": Comp.ZnCl3_minus,
        "ZnOH+": Comp.ZnOH_plus,
        "HZnO2-": Comp.HZnO2_minus,
        "ZnO2--": Comp.ZnO2_minus2,
        "UOH++": Comp.U_OH_plus2,
        "UO+": Comp.UO_plus,
        "U(OH)+++": Comp.U_OH_plus3,
        "UO++": Comp.UO_plus2,
        "HUO2+": Comp.HUO2_plus,
        "HUO3-": Comp.HUO3_minus,
        "UO3-": Comp.UO3_minus,
        "UO2OH+": Comp.UO2OH_plus,
        "HUO4-": Comp.HUO4_minus,
        "UO4--": Comp.UO4_minus2,
        "Fr+": Comp.Fr_plus,
        "OCN-": Comp.OCN_minus,
        "SCN-": Comp.SCN_minus,
        "SeCN-": Comp.SeCN_minus,
        "HN2O2-": Comp.HNO2_minus,
        "N2O2--": Comp.N2O2_minus2,
        "N2H5+": Comp.N2H5_plus,
        "N2H6++": Comp.N2H6_plus2,
        "H2PO2-": Comp.H2PO2_minus,
        "H2PO3-": Comp.H2PO3_minus,
        "HPO3--": Comp.HPO3_minus2,
        "P2O7----": Comp.P2O7_minus4,
        "HP2O7---": Comp.HP2O7_minus3,
        "AsO4---": Comp.AsO4_minus3,
        "AsO2-": Comp.AsO2_minus,
        "SbO2-": Comp.SbO2_minus,
        "Bi+++": Comp.Bi_plus3,
        "BiO+": Comp.BiO_plus,
        "BiOH++": Comp.BiOH_plus2,
        "BiO2-": Comp.BiO2_minus,
        "V++": Comp.V_plus2,
        "V+++": Comp.V_plus3,
        "VO4---": Comp.VO4_minus3,
        "Cr++": Comp.Cr_plus2,
        "Cr+++": Comp.Cr_plus3,
        "CrOH++": Comp.CrOH_plus2,
        "CrO+": Comp.CrO_plus,
        "CrO2-": Comp.CrO2_minus,
        "Zr++++": Comp.Zr_plus4,
        "ZrOH+++": Comp.Zr_OH_plus3,
        "ZrO++": Comp.ZrO_plus2,
        "HZrO2+": Comp.HZrO2_plus,
        "HZrO3-": Comp.HZrO3_minus,
        "NbO3-": Comp.NbO3_minus,
        "TcO4-": Comp.TcO4_minus,
        "Pm++": Comp.Pm_plus2,
        "Pm+++": Comp.Pm_plus3,
        "Pm++++": Comp.Pm_plus4,
        "Hf++++": Comp.Hf_plus4,
        "HfOH+++": Comp.HfOH_plus3,
        "HfO++": Comp.HfO_plus2,
        "HHfO2+": Comp.HHfO2_plus,
        "HHfO3-": Comp.HHfO3_minus,
        "La++": Comp.La_plus2,
        "LaCO3+": Comp.LaCO3_plus,
        "LaHCO3++": Comp.LaHCO3_plus2,
        "LaOH++": Comp.LaOH_plus2,
        "LaO+": Comp.LaO_plus,
        "LaO2-": Comp.LaO2_minus,
        "LaCl++": Comp.LaCl_plus2,
        "LaCl2+": Comp.LaCl2_plus,
        "LaCl4-": Comp.LaCl4_minus,
        "LaNO3++": Comp.LaNO3_plus2,
        "LaF++": Comp.LaF_plus2,
        "LaF2+": Comp.LaF2_plus,
        "LaF4-": Comp.LaF4_minus,
        "LaH2PO4++": Comp.LaH2PO4_plus2,
        "LaSO4+": Comp.LaSO4_plus,
        "CeCO3+": Comp.CeCO3_plus,
        "CeHCO3++": Comp.CeHCO3_plus2,
        "CeOH++": Comp.CeOH_plus2,
        "CeO+": Comp.CeO_plus,
        "CeO2-": Comp.CeO2_minus,
        "CeCl++": Comp.CeCl_plus2,
        "CeCl2+": Comp.CeCl2_plus,
        "CeCl4-": Comp.CeCl4_minus,
        "CeH2PO4++": Comp.CeH2PO4_plus2,
        "CeNO3++": Comp.CeNO3_plus2,
        "CeF++": Comp.CeF_plus2,
        "CeF2+": Comp.CeF2_plus,
        "CeF4-": Comp.CeF4_minus,
        "CeBr++": Comp.CeBr_plus2,
        "CeIO3++": Comp.CeIO3_plus2,
        "CeClO4++": Comp.CeClO4_plus2,
        "CeSO4+": Comp.CeSO4_plus,
        "PrCO3+": Comp.PrCO3_plus,
        "PrHCO3++": Comp.PrHCO3_plus2,
        "PrCl++": Comp.PrCl_plus2,
        "PrCl2+": Comp.PrCl2_plus,
        "PrCl4-": Comp.PrCl4_minus,
        "PrH2PO4++": Comp.PrH2PO4_plus2,
        "PrNO3++": Comp.PrNO3_plus2,
        "PrF++": Comp.PrF_plus2,
        "PrF2+": Comp.PrF2_plus,
        "PrF4-": Comp.PrF4_minus,
        "PrOH++": Comp.PrOH_plus2,
        "PrO+": Comp.PrO_plus,
        "PrO2-": Comp.PrO2_minus,
        "PrSO4+": Comp.PrSO4_plus,
        "NdCO3+": Comp.NdCO3_plus,
        "NdHCO3++": Comp.NdHCO3_plus2,
        "NdOH++": Comp.NdOH_plus2,
        "NdO+": Comp.NdO_plus,
        "NdO2-": Comp.NdO2_minus,
        "NdCl++": Comp.NdCl_plus2,
        "NdCl2+": Comp.NdCl2_plus,
        "NdCl4-": Comp.NdCl4_minus,
        "NdH2PO4++": Comp.NdH2PO4_plus2,
        "NdNO3++": Comp.NdNO3_plus2,
        "NdF++": Comp.NdF_plus2,
        "NdF2+": Comp.NdF2_plus,
        "NdF4-": Comp.NdF4_minus,
        "NdSO4+": Comp.NdSO4_plus,
        "SmCO3+": Comp.SmCO3_plus,
        "SmOH++": Comp.SmOH_plus2,
        "SmO+": Comp.SmO_plus,
        "SmO2-": Comp.SmO2_minus,
        "SmHCO3++": Comp.SmHCO3_plus2,
        "SmCl++": Comp.SmCl_plus2,
        "SmCl2+": Comp.SmCl2_plus,
        "SmCl4-": Comp.SmCl4_minus,
        "SmH2PO4++": Comp.SmH2PO4_plus2,
        "SmNO3++": Comp.SmNO3_plus2,
        "SmF++": Comp.SmF_plus2,
        "SmF2+": Comp.SmF2_plus,
        "SmF4-": Comp.SmF4_minus,
        "SmSO4+": Comp.SmSO4_plus,
        "EuCO3+": Comp.EuCO3_plus,
        "EuOH++": Comp.EuOH_plus2,
        "EuO+": Comp.EuO_plus,
        "EuO2-": Comp.EuO2_minus,
        "EuHCO3++": Comp.EuHCO3_plus2,
        "EuCl++": Comp.EuCl_plus2,
        "EuCl2+": Comp.EuCl2_plus,
        "EuCl4-": Comp.EuCl4_minus,
        "EuF+": Comp.EuF_plus,
        "EuF3-": Comp.EuF3_minus,
        "EuF4--": Comp.EuF4_minus2,
        "EuCl+": Comp.EuCl_plus,
        "EuCl3-": Comp.EuCl3_minus,
        "EuCl4--": Comp.EuCl4_minus2,
        "EuH2PO4++": Comp.EuH2PO4_plus2,
        "EuNO3++": Comp.EuNO3_plus2,
        "EuF++": Comp.EuF_plus2,
        "EuF2+": Comp.EuF2_plus,
        "EuF4-": Comp.EuF4_minus,
        "EuSO4+": Comp.EuSO4_plus,
        "GdCO3+": Comp.GdCO3_plus,
        "GdOH++": Comp.GdOH_plus2,
        "GdO+": Comp.GdO_plus,
        "GdO2-": Comp.GdO2_minus,
        "GdHCO3++": Comp.GdHCO3_plus2,
        "GdCl++": Comp.GdCl_plus2,
        "GdCl2+": Comp.GdCl2_plus,
        "GdCl4-": Comp.GdCl4_minus,
        "GdH2PO4++": Comp.GdH2PO4_plus2,
        "GdNO3++": Comp.GdNO3_plus2,
        "GdF++": Comp.GdF_plus2,
        "GdF2+": Comp.GdF2_plus,
        "GdF4-": Comp.GdF4_minus,
        "GdSO4+": Comp.GdSO4_plus,
        "TbCO3+": Comp.TbCO3_plus,
        "TbOH++": Comp.TbOH_plus2,
        "TbO+": Comp.TbO_plus,
        "TbO2-": Comp.TbO2_minus,
        "TbHCO3++": Comp.TbHCO3_plus2,
        "TbCl++": Comp.TbCl_plus2,
        "TbCl2+": Comp.TbCl2_plus,
        "TbCl4-": Comp.TbCl4_minus,
        "TbH2PO4++": Comp.TbH2PO4_plus2,
        "TbNO3++": Comp.TbNO3_plus2,
        "TbF++": Comp.TbF_plus2,
        "TbF2+": Comp.TbF2_plus,
        "TbF4-": Comp.TbF4_minus,
        "TbSO4+": Comp.TbSO4_plus,
        "DyCO3+": Comp.DyCO3_plus,
        "DyHCO3++": Comp.DyHCO3_plus2,
        "DyCl++": Comp.DyCl_plus2,
        "DyCl2+": Comp.DyCl2_plus,
        "DyCl4-": Comp.DyCl4_minus,
        "DyH2PO4++": Comp.DyH2PO4_plus2,
        "DyNO3++": Comp.DyNO3_plus2,
        "DyF++": Comp.DyF_plus2,
        "DyF2+": Comp.DyF2_plus,
        "DyF4-": Comp.DyF4_minus,
        "DyOH++": Comp.DyOH_plus2,
        "DyO+": Comp.DyO_plus,
        "DyO2-": Comp.DyO2_minus,
        "DySO4+": Comp.DySO4_plus,
        "HoCO3+": Comp.HoCO3_plus,
        "HoHCO3++": Comp.HoHCO3_plus2,
        "HoCl++": Comp.HoCl_plus2,
        "HoCl2+": Comp.HoCl2_plus,
        "HoCl4-": Comp.HoCl4_minus,
        "HoH2PO4++": Comp.HoH2PO4_plus2,
        "HoNO3++": Comp.HoNO3_plus2,
        "HoF++": Comp.HoF_plus2,
        "HoF2+": Comp.HoF2_plus,
        "HoF4-": Comp.HoF4_minus,
        "HoOH++": Comp.HoOH_plus2,
        "HoO+": Comp.HoO_plus,
        "HoO2-": Comp.HoO2_minus,
        "HoSO4+": Comp.HoSO4_plus,
        "ErCO3+": Comp.ErCO3_plus,
        "ErHCO3++": Comp.ErHCO3_plus2,
        "ErCl++": Comp.ErCl_plus2,
        "ErCl2+": Comp.ErCl2_plus,
        "ErCl4-": Comp.ErCl4_minus,
        "ErH2PO4++": Comp.ErH2PO4_plus2,
        "ErNO3++": Comp.ErNO3_plus2,
        "ErF++": Comp.ErF_plus2,
        "ErF2+": Comp.ErF2_plus,
        "ErF4-": Comp.ErF4_minus,
        "ErOH++": Comp.ErOH_plus2,
        "ErO+": Comp.ErO_plus,
        "ErO2-": Comp.ErO2_minus,
        "ErSO4+": Comp.ErSO4_plus,
        "TmCO3+": Comp.TmCO3_plus,
        "TmHCO3++": Comp.TmHCO3_plus2,
        "TmCl++": Comp.TmCl_plus2,
        "TmCl2+": Comp.TmCl2_plus,
        "TmCl4-": Comp.TmCl4_minus,
        "TmH2PO4++": Comp.TmH2PO4_plus2,
        "TmNO3++": Comp.TmNO3_plus2,
        "TmF++": Comp.TmF_plus2,
        "TmF2+": Comp.TmF2_plus,
        "TmF4-": Comp.TmF4_minus,
        "TmOH++": Comp.TmOH_plus2,
        "TmO+": Comp.TmO_plus,
        "TmO2-": Comp.TmO2_minus,
        "TmSO4+": Comp.TmSO4_plus,
        "YbCO3+": Comp.YbCO3_plus,
        "YbOH++": Comp.YbOH_plus2,
        "YbO+": Comp.YbO_plus,
        "YbO2-": Comp.YbO2_minus,
        "YbHCO3++": Comp.YbHCO3_plus2,
        "YbCl++": Comp.YbCl_plus2,
        "YbCl2+": Comp.YbCl2_plus,
        "YbCl4-": Comp.YbCl4_minus,
        "YbH2PO4++": Comp.YbH2PO4_plus2,
        "YbNO3++": Comp.YbNO3_plus2,
        "YbF++": Comp.YbF_plus2,
        "YbF2+": Comp.YbF2_plus,
        "YbF4-": Comp.YbF4_minus,
        "YbSO4+": Comp.YbSO4_plus,
        "LuCO3+": Comp.LuCO3_plus,
        "LuOH++": Comp.LuOH_plus2,
        "LuO+": Comp.LuO_plus,
        "LuO2-": Comp.LuO2_minus,
        "LuHCO3++": Comp.LuHCO3_plus2,
        "LuCl++": Comp.LuCl_plus2,
        "LuCl2+": Comp.LuCl2_plus,
        "LuCl4-": Comp.LuCl4_minus,
        "LuH2PO4++": Comp.LuH2PO4_plus2,
        "LuNO3++": Comp.LuNO3_plus2,
        "LuF++": Comp.LuF_plus2,
        "LuF2+": Comp.LuF2_plus,
        "LuF4-": Comp.LuF4_minus,
        "LuSO4+": Comp.LuSO4_plus,
        "NaSO4-": Comp.NaSO4_minus,
        "BeCl+": Comp.BeCl_plus,
        "FeCl++": Comp.FeCl_plus2,
        "CoCl+": Comp.CoCl_plus,
        "CuCl2-": Comp.CuCl2_minus,
        "CuCl3--": Comp.CuCl3_minus2,
        "CuCl+": Comp.CuCl_plus,
        "CuCl3-": Comp.CuCl3_minus,
        "CuCl4--": Comp.CuCl4_minus2,
        "CdCl+": Comp.CdCl_plus,
        "CdCl3-": Comp.CdCl3_minus,
        "CdCl4--": Comp.CdCl4_minus2,
        "TlCl++": Comp.TlCl_plus2,
        "AuCl2-": Comp.AuCl2_minus,
        "AuCl3--": Comp.AuCl3_minus2,
        "AuCl4-": Comp.AuCl4_minus,
        "HgCl+": Comp.HgCl_plus,
        "HgCl3-": Comp.HgCl3_minus,
        "HgCl4--": Comp.HgCl4_minus2,
        "InCl++": Comp.InCl_plus2,
        "BeF+": Comp.BeF_plus,
        "BeF3-": Comp.BeF3_minus,
        "BeF4--": Comp.BeF4_minus2,
        "MnF+": Comp.MnF_plus,
        "FeF+": Comp.FeF_plus,
        "FeF++": Comp.FeF_plus2,
        "CoF+": Comp.CoF_plus,
        "NiF+": Comp.NiF_plus,
        "CuF+": Comp.CuF_plus,
        "ZnF+": Comp.ZnF_plus,
        "CdF+": Comp.CdF_plus,
        "BaF+": Comp.BaF_plus,
        "HgF+": Comp.HgF_plus,
        "InF++": Comp.InF_plus2,
        "PbF+": Comp.PbF_plus,
        "Ag(HS)2-": Comp.Ag_HS_2_minus,
        "Au(HS)2-": Comp.Au_HS_2_minus,
        "Pb(HS)3-": Comp.Pb_HS_3_minus,
        "Mg(HSiO3)+": Comp.Mg_HSiO3_plus,
        "Ca(HSiO3)+": Comp.Ca_HSiO3_plus,
        "Akermanite": Comp.Akermanite,
        "Alabandite": Comp.Alabandite,
        "Albite,low": Comp.Albite_low,
        "Alunite": Comp.Alunite,
        "Amesite,7A": Comp.Amesite_7A,
        "Amorphous-Silica": Comp.Amorphous_Silica,
        "Analcime": Comp.Analcime,
        "Analcime,dehydrated": Comp.Analcime_dehydrated,
        "Andalusite": Comp.Andalusite,
        "Andradite": Comp.Andradite,
        "Anglesite": Comp.Anglesite,
        "Anhydrite": Comp.Anhydrite,
        "Annite": Comp.Annite,
        "Anorthite": Comp.Anorthite,
        "Aragonite": Comp.Aragonite,
        "Artinite": Comp.Artinite,
        "Azurite": Comp.Azurite,
        "Barite": Comp.Barite,
        "Berndtite": Comp.Berndtite,
        "Boehmite": Comp.Boehmite,
        "Bromellite": Comp.Bromellite,
        "Brucite": Comp.Brucite,
        "Ca-Al-Pyroxene": Comp.Ca_Al_Pyroxene,
        "Calcite": Comp.Calcite,
        "Cassiterite": Comp.Cassiterite,
        "Celadonite": Comp.Celadonite,
        "Celestite": Comp.Celestite,
        "Cerussite": Comp.Cerussite,
        "Chabazite": Comp.Chabazite,
        "Chalcedony": Comp.Chalcedony,
        "Chlorargyrite": Comp.Chlorargyrite,
        "Chloritoid": Comp.Chloritoid,
        "Chrysotile": Comp.Chrysotile,
        "Cinnabar": Comp.Cinnabar,
        "Clinochlore,14A": Comp.Clinochlore_14A,
        "Clinozoisite": Comp.Clinozoisite,
        "Copper": Comp.Copper,
        "Cordierite": Comp.Cordierite,
        "Cordierite,hydrous": Comp.Cordierite_hydrous,
        "Corundum": Comp.Corundum,
        "Covellite": Comp.Covellite,
        "Cristobalite,alpha": Comp.Cristobalite_alpha,
        "Cristobalite,beta": Comp.Cristobalite_beta,
        "Cummingtonite": Comp.Cummingtonite,
        "Cuprite": Comp.Cuprite,
        "Daphnite,14A": Comp.Daphnite_14A,
        "Diaspore": Comp.Diaspore,
        "Dickite": Comp.Dickite,
        "Diopside": Comp.Diopside,
        "Dolomite": Comp.Dolomite,
        "Dolomite,dis": Comp.Dolomite_dis,
        "Dolomite,ord": Comp.Dolomite_ord,
        "Epidote": Comp.Epidote,
        "Epidote,ord": Comp.Epidote_ord,
        "Fayalite": Comp.Fayalite,
        "Ferropargasite": Comp.Ferropargasite,
        "Ferrotremolite": Comp.Ferrotremolite,
        "Ferrous-Oxide": Comp.Ferrous_Oxide,
        "Fluorite": Comp.Fluorite,
        "Fluorphlogopite": Comp.Fluorphlogopite,
        "Fluortremolite": Comp.Fluortremolite,
        "Forsterite": Comp.Forsterite,
        "Galena": Comp.Galena,
        "Gehlenite": Comp.Gehlenite,
        "Gibbsite": Comp.Gibbsite,
        "Glaucophane": Comp.Glaucophane,
        "Gold": Comp.Gold,
        "Graphite": Comp.Graphite,
        "Greenalite": Comp.Greenalite,
        "Grossular": Comp.Grossular,
        "Grunerite": Comp.Grunerite,
        "Halite": Comp.Halite,
        "Halloysite": Comp.Halloysite,
        "Hedenbergite": Comp.Hedenbergite,
        "Huntite": Comp.Huntite,
        "Hydromagnesite": Comp.Hydromagnesite,
        "Jadeite": Comp.Jadeite,
        "K-Feldspar": Comp.K_Feldspar,
        "Kaolinite": Comp.Kaolinite,
        "Kyanite": Comp.Kyanite,
        "Laurite": Comp.Laurite,
        "Laumontite": Comp.Laumontite,
        "Leonhardite": Comp.Leonhardite,
        "Lime": Comp.Lime,
        "Magnesite": Comp.Magnesite,
        "Malachite": Comp.Malachite,
        "Manganosite": Comp.Manganosite,
        "Merwinite": Comp.Merwinite,
        "Metacinnabar": Comp.Metacinnabar,
        "Microcline,maximum": Comp.Microcline_maximum,
        "Minnesotaite": Comp.Minnesotaite,
        "Monticellite": Comp.Monticellite,
        "Muscovite": Comp.Muscovite,
        "Nepheline": Comp.Nepheline,
        "Palladium": Comp.Palladium,
        "Paragonite": Comp.Paragonite,
        "Pargasite": Comp.Pargasite,
        "Periclase": Comp.Periclase,
        "Phlogopite": Comp.Phlogopite,
        "Platinum": Comp.Platinum,
        "Potassium-Oxide": Comp.Potassium_Oxide,
        "Pyrite": Comp.Pyrite,
        "Pyrophyllite": Comp.Pyrophyllite,
        "Pd(OH2": Comp.Pd_OH_2,
        "Pd4S": Comp.Pd4S,
        "PdO": Comp.PdO,
        "PdS": Comp.PdS,
        "PtS": Comp.PtS,
        "PtS2": Comp.PtS2,
        "Rhodium": Comp.Rhodium,
        "Rhodochrosite": Comp.Rhodochrosite,
        "Richterite": Comp.Richterite,
        "Romarchite": Comp.Romarchite,
        "Ruthenium": Comp.Ruthenium,
        "Rutile": Comp.Rutile,
        "Rh2O": Comp.Rh2O,
        "Rh2O3": Comp.Rh2O3,
        "RuO2": Comp.RuO2,
        "Sanidine,high": Comp.Sanidine_high,
        "Sepiolite": Comp.Sepiolite,
        "Siderite": Comp.Siderite,
        "Sillimanite": Comp.Sillimanite,
        "Silver": Comp.Silver,
        "Smithsonite": Comp.Smithsonite,
        "Sodium-Oxide": Comp.Sodium_Oxide,
        "Sphalerite": Comp.Sphalerite,
        "Spinel": Comp.Spinel,
        "Staurolite": Comp.Staurolite,
        "Strontianite": Comp.Strontianite,
        "Sylvite": Comp.Sylvite,
        "Talc": Comp.Talc,
        "Tenorite": Comp.Tenorite,
        "Titanite": Comp.Titanite,
        "Tremolite": Comp.Tremolite,
        "Uraninite": Comp.Uraninite,
        "PdS2": Comp.PdS2,
        "Wairakite": Comp.Wairakite,
        "Wollastonite": Comp.Wollastonite,
        "Wurtzite": Comp.Wurtzite,
        "Zincite": Comp.Zincite,
        "Zoisite": Comp.Zoisite,
        "Litharge": Comp.Litharge,
        "Albite": Comp.Albite,
        "Albite,high": Comp.Albite_high,
        "Almandine": Comp.Almandine,
        "Amesite,14A": Comp.Amesite_14A,
        "Antigorite": Comp.Antigorite,
        "Clinochlore,7A": Comp.Clinochlore_7A,
        "Coesite": Comp.Coesite,
        "Cristobalite": Comp.Cristobalite,
        "Daphnite,7A": Comp.Daphnite_7A,
        "Edenite": Comp.Edenite,
        "Epistilbite": Comp.Epistilbite,
        "Ferroedenite": Comp.Ferroedenite,
        "Ferrosilite": Comp.Ferrosilite,
        "Fluoredenite": Comp.Fluoredenite,
        "Heulandite": Comp.Heulandite,
        "Kalsilite": Comp.Kalsilite,
        "Lawsonite": Comp.Lawsonite,
        "Magnetite": Comp.Magnetite,
        "Margarite": Comp.Margarite,
        "Natrolite": Comp.Natrolite,
        "Nesquehonite": Comp.Nesquehonite,
        "Nickel": Comp.Nickel,
        "Phillipsite,Ca": Comp.Phillipsite_Ca,
        "Phillipsite,K": Comp.Phillipsite_K,
        "Phillipsite,Na": Comp.Phillipsite_Na,
        "Prehnite": Comp.Prehnite,
        "Pyrope": Comp.Pyrope,
        "Quartz": Comp.Quartz,
        "Quicksilver": Comp.Quicksilver,
        "Spessartine": Comp.Spessartine,
        "Stilbite": Comp.Stilbite,
        "Tin": Comp.Tin,
        "Acanthite": Comp.Acanthite,
        "Aegerine": Comp.Aegerine,
        "Anthophyllite": Comp.Anthophyllite,
        "Bornite": Comp.Bornite,
        "Bunsenite": Comp.Bunsenite,
        "Chalcocite": Comp.Chalcocite,
        "Chalcopyrite": Comp.Chalcopyrite,
        "Cronstedtite,7A": Comp.Cronstedtite_7A,
        "Enstatite": Comp.Enstatite,
        "Ferrogedrite": Comp.Ferrogedrite,
        "Hastingsite": Comp.Hastingsite,
        "Hematite": Comp.Hematite,
        "Larnite": Comp.Larnite,
        "Magnesiohastingsite": Comp.Magnesiohastingsite,
        "Magnesioriebeckite": Comp.Magnesioriebeckite,
        "Pyrrhotite": Comp.Pyrrhotite,
        "Riebeckite": Comp.Riebeckite,
        "Sulfur": Comp.Sulfur,
        "Pd-Oxyannite": Comp.Pd_Oxyannite,
        "AgCl(aq)": Comp.AgCl_aq,
        "AgOH(aq)": Comp.AgOH_aq,
        "AgNO3(aq)": Comp.AgNO3_aq,
        "HAlO2(aq)": Comp.HAlO2_aq,
        "B(OH3(aq)": Comp.B_OH_3_aq,
        "BeO(aq)": Comp.BeO_aq,
        "HBrO(aq)": Comp.HBrO_aq,
        "HCN(aq)": Comp.HCN_aq,
        "CO(aq)": Comp.CO_aq,
        "CO2(aq)": Comp.CO2_aq,
        "CaCl2(aq)": Comp.CaCl2_aq,
        "CaSO4(aq)": Comp.CaSO4_aq,
        "CdO(aq)": Comp.CdO_aq,
        "HClO(aq)": Comp.HClO_aq,
        "CoO(aq)": Comp.CoO_aq,
        "CsBr(aq)": Comp.CsBr_aq,
        "CsCl(aq)": Comp.CsCl_aq,
        "CsI(aq)": Comp.CsI_aq,
        "CsOH(aq)": Comp.CsOH_aq,
        "CuO(aq)": Comp.CuO_aq,
        "FeCl2(aq)": Comp.FeCl2_aq,
        "FeO(aq)": Comp.FeO_aq,
        "HFeO2(aq)": Comp.HFeO2_aq,
        "HGaO2(aq)": Comp.HGaO2_aq,
        "H2(aq)": Comp.H2_aq,
        "H2S(aq)": Comp.H2S_aq,
        "H3VO4(aq)": Comp.H3VO4_aq,
        "H3PO4(aq)": Comp.H3PO4_aq,
        "HF(aq)": Comp.HF_aq,
        "HNO3(aq)": Comp.HNO3_aq,
        "H2SeO3(aq)": Comp.H2SeO3_aq,
        "He(aq)": Comp.He_aq,
        "HgO(aq)": Comp.HgO_aq,
        "HIO(aq)": Comp.HIO_aq,
        "HInO2(aq)": Comp.HInO2_aq,
        "KBr(aq)": Comp.KBr_aq,
        "KCl(aq)": Comp.KCl_aq,
        "KHSO4(aq)": Comp.KHSO4_aq,
        "KI(aq)": Comp.KI_aq,
        "KOH(aq)": Comp.KOH_aq,
        "Kr(aq)": Comp.Kr_aq,
        "LiCl(aq)": Comp.LiCl_aq,
        "LiOH(aq)": Comp.LiOH_aq,
        "MnO(aq)": Comp.MnO_aq,
        "MnSO4(aq)": Comp.MnSO4_aq,
        "N2(aq)": Comp.N2_aq,
        "NH3(aq)": Comp.NH3_aq,
        "NaBr(aq)": Comp.NaBr_aq,
        "NaCl(aq)": Comp.NaCl_aq,
        "NaF(aq)": Comp.NaF_aq,
        "NaHSiO3(aq)": Comp.NaHSiO3_aq,
        "NaI(aq)": Comp.NaI_aq,
        "NaOH(aq)": Comp.NaOH_aq,
        "Ne(aq)": Comp.Ne_aq,
        "NiO(aq)": Comp.NiO_aq,
        "O2(aq)": Comp.O2_aq,
        "PbCl2(aq)": Comp.PbCl2_aq,
        "PbO(aq)": Comp.PbO_aq,
        "PdSO4(aq)": Comp.PdSO4_aq,
        "PdCl2(aq)": Comp.PdCl2_aq,
        "PdO(aq)": Comp.PdO_aq,
        "PtSO4(aq)": Comp.PtSO4_aq,
        "PtCl2(aq)": Comp.PtCl2_aq,
        "PtO(aq)": Comp.PtO_aq,
        "RbBr(aq)": Comp.RbBr_aq,
        "RbCl(aq)": Comp.RbCl_aq,
        "RbF(aq)": Comp.RbF_aq,
        "RbI(aq)": Comp.RbI_aq,
        "RbOH(aq)": Comp.RbOH_aq,
        "RhSO4(aq)": Comp.RhSO4_aq,
        "RhCl2(aq)": Comp.RhCl2_aq,
        "RhCl3(aq)": Comp.RhCl3_aq,
        "RhO(aq)": Comp.RhO_aq,
        "Rn(aq)": Comp.Rn_aq,
        "RuSO4(aq)": Comp.RuSO4_aq,
        "RuCl2(aq)": Comp.RuCl2_aq,
        "RuCl3(aq)": Comp.RuCl3_aq,
        "RuO(aq)": Comp.RuO_aq,
        "H2S2O3(aq)": Comp.H2S2O3_aq,
        "H2S2O4(aq)": Comp.H2S2O4_aq,
        "SO2(aq)": Comp.SO2_aq,
        "HScO2(aq)": Comp.HScO2_aq,
        "SiO2(aq)": Comp.SiO2_aq,
        "SnO(aq)": Comp.SnO_aq,
        "TlOH(aq)": Comp.TlOH_aq,
        "HTlO2(aq)": Comp.HTlO2_aq,
        "Xe(aq)": Comp.Xe_aq,
        "HYO2(aq)": Comp.HYO2_aq,
        "ZnCl2(aq)": Comp.ZnCl2_aq,
        "ZnO(aq)": Comp.ZnO_aq,
        "HUO2(aq)": Comp.HUO2_aq,
        "UO2(aq)": Comp.UO2_aq,
        "UO2OH(aq)": Comp.UO2OH_aq,
        "UO3(aq)": Comp.UO3_aq,
        "HNO2(aq)": Comp.HNO2_aq,
        "H2N2O2(aq)": Comp.H2N2O2_aq,
        "H3PO2(aq)": Comp.H3PO2_aq,
        "H3PO3(aq)": Comp.H3PO3_aq,
        "H4P2O7(aq)": Comp.H4P2O7_aq,
        "H3AsO4(aq)": Comp.H3AsO4_aq,
        "HAsO2(aq)": Comp.HAsO2_aq,
        "HSbO2(aq)": Comp.HSbO2_aq,
        "HBiO2(aq)": Comp.HBiO2_aq,
        "H2O2(aq)": Comp.H2O2_aq,
        "HClO2(aq)": Comp.HClO2_aq,
        "HIO3(aq)": Comp.HIO3_aq,
        "HCrO2(aq)": Comp.HCrO2_aq,
        "ZrO2(aq)": Comp.ZrO2_aq,
        "HNbO3(aq)": Comp.HNbO3_aq,
        "HfO2(aq)": Comp.HfO2_aq,
        "LaO2H(aq)": Comp.LaO2H_aq,
        "LaCl3(aq)": Comp.LaCl3_aq,
        "LaF3(aq)": Comp.LaF3_aq,
        "CeO2H(aq)": Comp.CeO2H_aq,
        "CeCl3(aq)": Comp.CeCl3_aq,
        "CeF3(aq)": Comp.CeF3_aq,
        "PrCl3(aq)": Comp.PrCl3_aq,
        "PrF3(aq)": Comp.PrF3_aq,
        "PrO2H(aq)": Comp.PrO2H_aq,
        "NdO2H(aq)": Comp.NdO2H_aq,
        "NdCl3(aq)": Comp.NdCl3_aq,
        "NdF3(aq)": Comp.NdF3_aq,
        "SmO2H(aq)": Comp.SmO2H_aq,
        "SmCl3(aq)": Comp.SmCl3_aq,
        "SmF3(aq)": Comp.SmF3_aq,
        "EuO2H(aq)": Comp.EuO2H_aq,
        "EuCl3(aq)": Comp.EuCl3_aq,
        "EuF2(aq)": Comp.EuF2_aq,
        "EuCl2(aq)": Comp.EuCl2_aq,
        "EuF3(aq)": Comp.EuF3_aq,
        "GdO2H(aq)": Comp.GdO2H_aq,
        "GdCl3(aq)": Comp.GdCl3_aq,
        "GdF3(aq)": Comp.GdF3_aq,
        "TbO2H(aq)": Comp.TbO2H_aq,
        "TbCl3(aq)": Comp.TbCl3_aq,
        "TbF3(aq)": Comp.TbF3_aq,
        "DyCl3(aq)": Comp.DyCl3_aq,
        "DyF3(aq)": Comp.DyF3_aq,
        "DyO2H(aq)": Comp.DyO2H_aq,
        "HoCl3(aq)": Comp.HoCl3_aq,
        "HoF3(aq)": Comp.HoF3_aq,
        "HoO2H(aq)": Comp.HoO2H_aq,
        "ErCl3(aq)": Comp.ErCl3_aq,
        "ErF3(aq)": Comp.ErF3_aq,
        "ErO2H(aq)": Comp.ErO2H_aq,
        "TmCl3(aq)": Comp.TmCl3_aq,
        "TmF3(aq)": Comp.TmF3_aq,
        "TmO2H(aq)": Comp.TmO2H_aq,
        "YbO2H(aq)": Comp.YbO2H_aq,
        "YbCl3(aq)": Comp.YbCl3_aq,
        "YbF3(aq)": Comp.YbF3_aq,
        "LuO2H(aq)": Comp.LuO2H_aq,
        "LuCl3(aq)": Comp.LuCl3_aq,
        "LuF3(aq)": Comp.LuF3_aq,
        "MgSO4(aq)": Comp.MgSO4_aq,
        "HCl(aq)": Comp.HCl_aq,
        "MgCO3(aq)": Comp.MgCO3_aq,
        "CaCO3(aq)": Comp.CaCO3_aq,
        "SrCO3(aq)": Comp.SrCO3_aq,
        "BaCO3(aq)": Comp.BaCO3_aq,
        "BeCl2(aq)": Comp.BeCl2_aq,
        "CuCl(aq)": Comp.CuCl_aq,
        "CuCl2(aq)": Comp.CuCl2_aq,
        "CdCl2(aq)": Comp.CdCl2_aq,
        "TlCl(aq)": Comp.TlCl_aq,
        "AuCl(aq)": Comp.AuCl_aq,
        "HgCl2(aq)": Comp.HgCl2_aq,
        "BeF2(aq)": Comp.BeF2_aq,
        "AgF(aq)": Comp.AgF_aq,
        "CdF2(aq)": Comp.CdF2_aq,
        "TlF(aq)": Comp.TlF_aq,
        "PbF2(aq)": Comp.PbF2_aq,
        "Pb(HS2(aq)": Comp.Pb_HS_2_aq,
        "H2O(l": Comp.H2O_l,
        "H": Comp.H,
        "He": Comp.He,
        "Li": Comp.Li,
        "Be": Comp.Be,
        "B": Comp.B,
        "C": Comp.C,
        "N": Comp.N,
        "O": Comp.O,
        "F": Comp.F,
        "Ne": Comp.Ne,
        "Na": Comp.Na,
        "Mg": Comp.Mg,
        "Al": Comp.Al,
        "Si": Comp.Si,
        "P": Comp.P,
        "S": Comp.S,
        "Cl": Comp.Cl,
        "K": Comp.K,
        "Ar": Comp.Ar,
        "Ca": Comp.Ca,
        "Sc": Comp.Sc,
        "Ti": Comp.Ti,
        "V": Comp.V,
        "Cr": Comp.Cr,
        "Mn": Comp.Mn,
        "Fe": Comp.Fe,
        "Ni": Comp.Ni,
        "Co": Comp.Co,
        "Cu": Comp.Cu,
        "Zn": Comp.Zn,
        "Ga": Comp.Ga,
        "Ge": Comp.Ge,
        "As": Comp.As,
        "Se": Comp.Se,
        "Br": Comp.Br,
        "Kr": Comp.Kr,
        "Rb": Comp.Rb,
        "Sr": Comp.Sr,
        "Y": Comp.Y,
        "Zr": Comp.Zr,
        "Nb": Comp.Nb,
        "Mo": Comp.Mo,
        "Tc": Comp.Tc,
        "Ru": Comp.Ru,
        "Rh": Comp.Rh,
        "Pd": Comp.Pd,
        "Ag": Comp.Ag,
        "Cd": Comp.Cd,
        "In": Comp.In,
        "Sn": Comp.Sn,
        "Sb": Comp.Sb,
        "I": Comp.I,
        "Te": Comp.Te,
        "Xe": Comp.Xe,
        "Cs": Comp.Cs,
        "Ba": Comp.Ba,
        "La": Comp.La,
        "Ce": Comp.Ce,
        "Pr": Comp.Pr,
        "Nd": Comp.Nd,
        "Pm": Comp.Pm,
        "Sm": Comp.Sm,
        "Eu": Comp.Eu,
        "Gd": Comp.Gd,
        "Tb": Comp.Tb,
        "Dy": Comp.Dy,
        "Ho": Comp.Ho,
        "Er": Comp.Er,
        "Tm": Comp.Tm,
        "Yb": Comp.Yb,
        "Lu": Comp.Lu,
        "Hf": Comp.Hf,
        "Ta": Comp.Ta,
        "W": Comp.W,
        "Re": Comp.Re,
        "Os": Comp.Os,
        "Ir": Comp.Ir,
        "Pt": Comp.Pt,
        "Au": Comp.Au,
        "Hg": Comp.Hg,
        "Tl": Comp.Tl,
        "Pb": Comp.Pb,
        "Bi": Comp.Bi,
        "Po": Comp.Po,
        "At": Comp.At,
        "Rn": Comp.Rn,
        "Fr": Comp.Fr,
        "Ra": Comp.Ra,
        "Ac": Comp.Ac,
        "Pa": Comp.Pa,
        "Th": Comp.Th,
        "Np": Comp.Np,
        "U": Comp.U,
        "Am": Comp.Am,
        "Pu": Comp.Pu,
        "Bk": Comp.Bk,
        "Cm": Comp.Cm,
        "Cf": Comp.Cf,
        "Es": Comp.Es,
        "Fm": Comp.Fm,
        "Md": Comp.Md,
        "No": Comp.No,
        "Rf": Comp.Rf,
        "Lr": Comp.Lr}

    coolpropToComp = {
        "Water": Comp.WATER,
        "Hydrogen": Comp.H2_g,
        "Oxygen": Comp.O2_g,
        "Ammonia": Comp.AMMONIA_g,
        "CarbonDioxide": Comp.CARBONDIOXIDE,
        "Nitrogen": Comp.NITROGEN,
        "HydrogenSulfide": Comp.H2S,
        "Helium": Comp.He_g,
        "Argon": Comp.ARGON,
        "Methane": Comp.METHANE,
        "CarbonMonoxide": Comp.CO_g,
        "Ethylene": Comp.C2H4_g,
        "SulfurDioxide": Comp.SO2_g,
        "Krypton": Comp.Kr_g,
        "Neon": Comp.Ne_g,
        "Xenon": Comp.Xe_g}

    def withReaktoroName(self, name):
        return self.reaktoroToComp[name]

    def withCoolPropName(self, name):
        return self.coolpropToComp[name]

    def generate(self):

        self.reaktoroToComp = {}
        self.coolpropToComp = {}

        for i in Comp:

            if i.value.alias["RKT"] is not None:
                self.reaktoroToComp[i.value.alias["RKT"]] = i
            if i.value.alias["CP"] is not None:
                self.coolpropToComp[i.value.alias["CP"]] = i

        return self