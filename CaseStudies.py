import ThemophysicalPropertyModel as tppm
import pickle
import time
import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

# Maasland: MLD-GT-01-S1
if __name__ == "__main_":

    # lab conditions - assumed...
    T = 298
    P = 101325

    # the liquid phase composition
    liq_components = [tppm.Comp.WATER,
                      tppm.Comp.Ba,
                      tppm.Comp.Ca,
                      tppm.Comp.HCO3_minus,
                      tppm.Comp.Cl,
                      tppm.Comp.Fe,
                      tppm.Comp.K,
                      tppm.Comp.Mg,
                      tppm.Comp.Mn,
                      tppm.Comp.Na,
                      tppm.Comp.Sr,
                      tppm.Comp.SO4_minus2]
    liq_composition = [1e6,
                       6.1,
                       6200,
                       140,
                       68000,
                       84,
                       350,
                       680,
                       2.2,
                       38000,
                       360,
                       270]
    liq_composition = [i * 1e-6 for i in liq_composition]

    # creating the liquid fluid container
    liquid = tppm.Fluid(components=liq_components, composition=liq_composition)

    # perform a partition in order to get all aqueous species
    partition = tppm.Partition()
    partition.options.Reaktoro.speciesMode = tppm.PartitionModelOptions().Reaktoro.SpeciesMode.ALL
    liquid = partition.calc(liquid, P, T)

    liquid.cullComponents()  # remove all components under a certain mole threshold
    liquid.cullPhase(tppm.PhaseType.GASEOUS)  # remove any gaseous components

    # the liquid phase composition
    gas_components = [tppm.Comp.NITROGEN,
                      tppm.Comp.CARBONDIOXIDE,
                      tppm.Comp.METHANE]
    gas_composition = [4.136,
                       14.697,
                       81.167]
    # make sure the composition is scaled to 1 kg
    gas_tot = sum(gas_composition)
    gas_composition = [i / gas_tot for i in gas_composition]

    # create the gas fluid container
    gas = tppm.Fluid(components=gas_components, composition=gas_composition)

    # calculate the properties of the two fluids
    properties = tppm.PropertyModel()

    properties.calc(gas, P, T)

    properties.calc(liquid, P, T)

    # determine the mixing factor
    volume_ratio = 0.78  # the gas / liquid ratio from the lab report
    gas_volume = gas.total.props.v
    liquid_volume = liquid.total.props.v
    gas_scale_factor = volume_ratio / gas_volume * liquid_volume

    # blend the fluids accordingly
    total = tppm.Blender.blend(liquid, gas, gas_scale_factor)

    # define the reservoir conditions
    Tres = 273.15 + 95
    Pres = 2800 * 9.81 * 1000 + 101325

    # determine the partitioning at reservoir conditions, then calculate the fluid properties
    partition.options.Reaktoro.speciesMode = tppm.PartitionModelOptions().Reaktoro.SpeciesMode.SELECTED
    reservoir = partition.calc(total, Pres, Tres)
    properties.calc(reservoir, Pres, Tres)
    # print(reservoir)

    Pwh = 10 * 101325
    Twh = 273.15 + 99.8
    surface = partition.calc(reservoir, Pwh, Twh)
    properties.calc(surface, Pwh, Twh)

    print(surface)

    print(reservoir.total.props.h - surface.total.props.h)

# CoolProp Seawater comparison
if __name__ == "__main_":

    sal = 0.1
    comp = [tppm.Comp.WATER, tppm.Comp.Halite]
    mass = [1 , sal]
    brine = tppm.Fluid(components=comp, composition=mass)

    partition = tppm.Partition()
    brine = partition.calc(brine, 101325, 298)

    property = tppm.PropertyModel()

    n = 5
    p = 101325
    ts = np.linspace(298, 370, n)

    tppm_density = np.zeros(n)
    mitsw_density = np.zeros(n)
    iapws_density = np.zeros(n)

    tppm_enthalpy = np.zeros(n)
    mitsw_enthalpy = np.zeros(n)
    iapws_enthalpy = np.zeros(n)

    tppm_entropy = np.zeros(n)
    mitsw_entropy = np.zeros(n)
    iapws_entropy = np.zeros(n)

    for i, t in enumerate(ts):
        props = property.calc(brine, p, t)

        tppm_density[i] = props.total.props.rho
        mitsw_density[i] = PropsSI("D", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal))
        iapws_density[i] = PropsSI("D", "T", t, "P", p, "Water")

        tppm_enthalpy[i] = props.total.props.h
        mitsw_enthalpy[i] = PropsSI("H", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal))/1000
        iapws_enthalpy[i] = PropsSI("H", "T", t, "P", p, "Water")/1000

        tppm_entropy[i] = props.total.props.s
        mitsw_entropy[i] = PropsSI("S", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal))/1000
        iapws_entropy[i] = PropsSI("S", "T", t, "P", p, "Water")/1000

    ts = ts - 273.15

    diff_density = np.abs((tppm_density - mitsw_density)/(mitsw_density + 1e-6) * 100)
    print(diff_density)

    fig, ax1 = plt.subplots()
    ax1.set_title("Brine Density for {:} kg/kg NaCl".format(sal))
    ax2 = ax1.twinx()

    ax1.plot(ts, tppm_density, label="TPPM")
    ax1.plot(ts, mitsw_density, label="MITSW")
    ax1.plot(ts, iapws_density, label="IAPWS")

    ax2.plot(ts, diff_density, "r-", label="%diff")

    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Density, kg/m3")
    ax2.set_ylabel("Percentage Difference, %")

    ax1.legend()
    ax2.legend(loc=3)

    plt.tight_layout()
    plt.show()

    tppm_enthalpy = tppm_enthalpy - tppm_enthalpy[0]
    mitsw_enthalpy = mitsw_enthalpy - mitsw_enthalpy[0]
    iapws_enthalpy = iapws_enthalpy - iapws_enthalpy[0]
    diff_enthalpy = (tppm_enthalpy - mitsw_enthalpy) / (mitsw_enthalpy + 1e-6) *100
    print("___ENTHALPY___")
    print(tppm_enthalpy)
    print(mitsw_enthalpy)
    print(iapws_enthalpy)
    print(diff_enthalpy)

    fig, ax1 = plt.subplots()
    ax1.set_title("Brine Enthalpy for {:} kg/kg NaCl".format(sal))
    ax2 = ax1.twinx()

    ax1.plot(ts, tppm_enthalpy, label="TPPM")
    ax1.plot(ts, mitsw_enthalpy, label="MITSW")
    ax1.plot(ts, iapws_enthalpy, label="IAPWS")

    ax2.plot(ts[1:], diff_enthalpy[1:], "r-", label="%diff")

    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Enthalpy, kJ/kg")
    ax2.set_ylabel("Percentage Difference, %")

    ax1.legend()
    ax2.legend(loc=4)

    plt.tight_layout()
    plt.show()

    tppm_entropy = tppm_entropy - tppm_entropy[0]
    mitsw_entropy = mitsw_entropy - mitsw_entropy[0]
    iapws_entropy = iapws_entropy - iapws_entropy[0]
    diff_entropy = (tppm_entropy - mitsw_entropy) / (mitsw_entropy + 1e-6) *100
    print("___ENTROPY___")
    print(tppm_entropy)
    print(mitsw_entropy)
    print(iapws_entropy)
    print(diff_entropy)

    fig, ax1 = plt.subplots()
    ax1.set_title("Brine Entropy for {:} kg/kg NaCl".format(sal))
    ax2 = ax1.twinx()

    ax1.plot(ts, tppm_entropy, label="TPPM")
    ax1.plot(ts, mitsw_entropy, label="MITSW")
    ax1.plot(ts, iapws_entropy, label="IAPWS")

    ax2.plot(ts[1:], diff_entropy[1:], "r-", label="%diff")

    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Entropy, kJ/kg/K")
    ax2.set_ylabel("Percentage Difference, %")

    ax1.legend()
    ax2.legend(loc=4)

    plt.tight_layout()
    plt.show()

# CoolProp Lithium Bromide comparison
if __name__ == "__main_":

    from CoolProp.CoolProp import PropsSI
    import numpy as np
    import matplotlib.pyplot as plt

    sal = 0.05
    comp = [tppm.Comp.WATER, tppm.Comp.Li, tppm.Comp.Br]
    alpha = (tppm.Comp.Br.value.Mr / tppm.Comp.Li.value.Mr)

    mass = [1, sal/(1 + alpha), alpha * sal / (1 + alpha)]
    brine = tppm.Fluid(components=comp, composition=mass)

    partition = tppm.Partition()
    brine = partition.calc(brine, 101325, 298)

    property = tppm.PropertyModel()

    n = 5
    p = 101325
    ts = np.linspace(298, 370, n)

    tppm_density = np.zeros(n)
    mitsw_density = np.zeros(n)
    iapws_density = np.zeros(n)
    libr_density = np.zeros(n)

    tppm_enthalpy = np.zeros(n)
    mitsw_enthalpy = np.zeros(n)
    iapws_enthalpy = np.zeros(n)
    libr_enthalpy = np.zeros(n)

    tppm_entropy = np.zeros(n)
    mitsw_entropy = np.zeros(n)
    iapws_entropy = np.zeros(n)
    libr_entropy = np.zeros(n)

    for i, t in enumerate(ts):
        props = property.calc(brine, p, t)

        tppm_density[i] = props.total.props.rho
        libr_density[i] = PropsSI("D", "T", t, "P", p, "INCOMP::LiBr[{}]".format(sal))
        iapws_density[i] = PropsSI("D", "T", t, "P", p, "Water")

        tppm_enthalpy[i] = props.total.props.h
        libr_enthalpy[i] = PropsSI("H", "T", t, "P", p, "INCOMP::LiBr[{}]".format(sal))/1000
        iapws_enthalpy[i] = PropsSI("H", "T", t, "P", p, "Water")/1000

        tppm_entropy[i] = props.total.props.s
        libr_entropy[i] = PropsSI("S", "T", t, "P", p, "INCOMP::LiBr[{}]".format(sal))/1000
        iapws_entropy[i] = PropsSI("S", "T", t, "P", p, "Water")/1000

        if sal < 0.12:
            mitsw_density[i] = PropsSI("D", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal))
            mitsw_enthalpy[i] = PropsSI("H", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal)) / 1000
            mitsw_entropy[i] = PropsSI("S", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal)) / 1000

    ts = ts - 273.15

    diff_density = (tppm_density - libr_density)/(libr_density + 1e-6) * 100
    print(diff_density)

    fig, ax1 = plt.subplots()
    ax1.set_title("Brine Density for {:} kg/kg LiBr".format(sal))
    ax2 = ax1.twinx()

    ax1.plot(ts, tppm_density, label="TPPM")
    ax1.plot(ts, libr_density, label="LiBr")
    ax1.plot(ts, iapws_density, label="IAPWS")

    if sal < 0.12:
        ax1.plot(ts, mitsw_density, label="MITSW")

    ax2.plot(ts, diff_density, "r-", label="%diff")

    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Density, kg/m3")
    ax2.set_ylabel("Percentage Difference, %")

    ax1.legend()
    ax2.legend(loc=4)

    plt.tight_layout()
    plt.show()

    tppm_enthalpy = tppm_enthalpy - tppm_enthalpy[0]
    mitsw_enthalpy = mitsw_enthalpy - mitsw_enthalpy[0]
    libr_enthalpy = libr_enthalpy - libr_enthalpy[0]
    iapws_enthalpy = iapws_enthalpy - iapws_enthalpy[0]
    diff_enthalpy = (tppm_enthalpy - libr_enthalpy) / (libr_enthalpy + 1e-6) *100
    print("___ENTHALPY___")
    print(tppm_enthalpy)
    print(mitsw_enthalpy)
    print(libr_enthalpy)
    print(iapws_enthalpy)
    print(diff_enthalpy)

    fig, ax1 = plt.subplots()
    ax1.set_title("Brine Enthalpy for {:} kg/kg LiBr".format(sal))
    ax2 = ax1.twinx()

    ax1.plot(ts, tppm_enthalpy, label="TPPM")
    ax1.plot(ts, libr_enthalpy, label="LiBr")
    ax1.plot(ts, iapws_enthalpy, label="IAPWS")
    if sal < 0.12:
        ax1.plot(ts, mitsw_enthalpy, label="MITSW")

    ax2.plot(ts[1:], diff_enthalpy[1:], "r-", label="%diff")

    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Enthalpy, kJ/kg")
    ax2.set_ylabel("Percentage Difference, %")

    ax1.legend()
    ax2.legend(loc=4)

    plt.tight_layout()
    plt.show()

    tppm_entropy = tppm_entropy - tppm_entropy[0]
    libr_entropy = libr_entropy - libr_entropy[0]
    mitsw_entropy = mitsw_entropy - mitsw_entropy[0]
    iapws_entropy = iapws_entropy - iapws_entropy[0]
    diff_entropy = (tppm_entropy - libr_entropy) / (libr_entropy + 1e-6) *100
    print("___ENTROPY___")
    print(tppm_entropy)
    print(libr_entropy)
    print(mitsw_entropy)
    print(iapws_entropy)
    print(diff_entropy)

    fig, ax1 = plt.subplots()
    ax1.set_title("Brine Entropy for {:} kg/kg LiBr".format(sal))
    ax2 = ax1.twinx()

    ax1.plot(ts, tppm_entropy, label="TPPM")
    ax1.plot(ts, libr_entropy, label="LiBr")
    ax1.plot(ts, iapws_entropy, label="IAPWS")
    if sal < 0.12:
        ax1.plot(ts, mitsw_entropy, label="MITSW")

    ax2.plot(ts[1:], diff_entropy[1:], "r-", label="%diff")

    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Entropy, kJ/kg/K")
    ax2.set_ylabel("Percentage Difference, %")

    ax1.legend()
    ax2.legend(loc=4)

    plt.tight_layout()
    plt.show()

# composition template
    # liq_components = [tppm.Comp.WATER,
    #                   tppm.Comp.Al,
    #                   tppm.Comp.As,
    #                   tppm.Comp.B,
    #                   tppm.Comp.Ba,
    #                   tppm.Comp.Ca,
    #                   tppm.Comp.Cd,
    #                   tppm.Comp.Co,
    #                   tppm.Comp.Cr,
    #                   tppm.Comp.Cu,
    #                   tppm.Comp.Fe,
    #                   tppm.Comp.Hg,
    #                   tppm.Comp.K,
    #                   tppm.Comp.Li,
    #                   tppm.Comp.Mg,
    #                   tppm.Comp.Mn,
    #                   tppm.Comp.Mo,
    #                   tppm.Comp.Na,
    #                   tppm.Comp.Ni,
    #                   tppm.Comp.P,
    #                   tppm.Comp.Pb,
    #                   tppm.Comp.S,
    #                   tppm.Comp.Sb,
    #                   tppm.Comp.Se,
    #                   tppm.Comp.Si,
    #                   tppm.Comp.Sr,
    #                   tppm.Comp.Ti,
    #                   tppm.Comp.Tl,
    #                   tppm.Comp.V,
    #                   tppm.Comp.Zn,
    #                   tppm.Comp.Cl,
    #                   tppm.Comp.NO3_minus,
    #                   tppm.Comp.SO4_minus2,]
    # liq_composition = [1e6,
    #                    0.1,
    #                    0.1,
    #                    1.2,
    #                    0.1,
    #                    49.2,
    #                    0.1,
    #                    0.1,
    #                    0.1,
    #                    0.1,
    #                    0.1,
    #                    0.1,
    #                    10.2,
    #                    0.2,
    #                    32.9,
    #                    0.1,
    #                    0.1,
    #                    396,
    #                    0.1,
    #                    0.1,
    #                    0.1,
    #                    240,
    #                    0.1,
    #                    2.4,
    #                    13.8,
    #                    1.1,
    #                    0.1,
    #                    0.1,
    #                    0.1,
    #                    0.1,
    #                    152,
    #                    0.1,
    #                    749]
""" ______ """

# analysis of the Russian Fluid samples
if __name__ == "__main_":

    for i in ["Sample No68"]:
        liq_components = [tppm.Comp.WATER,
                          tppm.Comp.B,
                          tppm.Comp.Ca,
                          tppm.Comp.K,
                          tppm.Comp.Li,
                          tppm.Comp.Mg,
                          tppm.Comp.Na,
                          tppm.Comp.S,
                          tppm.Comp.Se,
                          tppm.Comp.Si,
                          tppm.Comp.Sr,
                          tppm.Comp.Cl,
                          tppm.Comp.SO4_minus2]
        liq_composition = [1e6,
                           1.2,
                           49.2,
                           10.2,
                           0.2,
                           32.9,
                           396,
                           240,
                           2.4,
                           13.8,
                           1.1,
                           152,
                           749]
        liq_composition = [i * 1e-6 for i in liq_composition]

        # creating the liquid fluid container
        fluid_No68 = tppm.Fluid(components=liq_components, composition=liq_composition)

        partition = tppm.Partition()

        fluid_No68 = partition.calc(fluid_No68, 101325, 273.15)
        fluid_No68.cullComponents()

    for i in ["Sample No129"]:
        liq_components = [tppm.Comp.WATER,
                          tppm.Comp.B,
                          tppm.Comp.Ca,
                          tppm.Comp.K,
                          tppm.Comp.Li,
                          tppm.Comp.Mg,
                          tppm.Comp.Na,
                          tppm.Comp.P,
                          tppm.Comp.S,
                          tppm.Comp.Se,
                          tppm.Comp.Si,
                          tppm.Comp.Sr,
                          tppm.Comp.Cl,
                          tppm.Comp.SO4_minus2]
        liq_composition = [1e6,
                           2.4,
                           2.8,
                           4.7,
                           0.1,
                           1.3,
                           590,
                           0.2,
                           211,
                           0.2,
                           12.3,
                           0.1,
                           176,
                           616]

        liq_composition = [i * 1e-6 for i in liq_composition]

        # creating the liquid fluid container
        fluid_No129 = tppm.Fluid(components=liq_components, composition=liq_composition)

        partition = tppm.Partition()

        fluid_No129 = partition.calc(fluid_No129, 101325, 298)
        fluid_No129.cullComponents()

    for i in ["Sample No27T"]:
        liq_components = [tppm.Comp.WATER,
                          tppm.Comp.B,
                          tppm.Comp.Ba,
                          tppm.Comp.Ca,
                          tppm.Comp.K,
                          tppm.Comp.Li,
                          tppm.Comp.Mg,
                          tppm.Comp.Na,
                          tppm.Comp.S,
                          tppm.Comp.Si,
                          tppm.Comp.Sr,
                          tppm.Comp.Cl,
                          tppm.Comp.SO4_minus2,
                          tppm.Comp.H_plus,
                          tppm.Comp.O2_aq]
        liq_composition = [1e6,
                           59.3,
                           1.7,
                           73.6,
                           145,
                           2.2,
                           28.5,
                           7540,
                           39.8,
                           29.4,
                           6.7,
                           7387,
                           30.7,
                           1,
                           1]

        liq_composition = [i * 1e-6 for i in liq_composition]

        # creating the liquid fluid container
        fluid_No27T = tppm.Fluid(components=liq_components, composition=liq_composition)

        partition = tppm.Partition()
        # partition.options.Reaktoro.strictSucess = False

        fluid_No27T = partition.calc(fluid_No27T, 101325, 300)
        fluid_No27T.cullComponents()
        fluid_No27T.cullPhase(tppm.PhaseType.GASEOUS)

    for i in ["Sample No38T"]:
        # reduced comp
        liq_components = [tppm.Comp.WATER,
                          tppm.Comp.B,
                          tppm.Comp.Ca,
                          tppm.Comp.K,
                          tppm.Comp.Li,
                          tppm.Comp.Mg,
                          tppm.Comp.Na,
                          tppm.Comp.S,
                          tppm.Comp.Si,
                          tppm.Comp.Sr,
                          tppm.Comp.Cl,
                          tppm.Comp.NO3_minus,
                          tppm.Comp.SO4_minus2,
                          tppm.Comp.H_plus,
                          tppm.Comp.O2_aq]
        liq_composition = [1e6,
                           59.8,
                           72.6,
                           138,
                           2.1,
                           29.6,
                           7660,
                           34.2,
                           28.1,
                           6.8,
                           7689,
                           59.3,
                           24.6,
                           1,
                           1]

        liq_composition = [i * 1e-6 for i in liq_composition]

        # creating the liquid fluid container
        fluid_No38T = tppm.Fluid(components=liq_components, composition=liq_composition)

        partition = tppm.Partition()
        # partition.options.Reaktoro.strictSucess = False

        fluid_No38T = partition.calc(fluid_No38T, 101325, 298)
        fluid_No38T.cullComponents()
        fluid_No38T.cullPhase(tppm.PhaseType.GASEOUS)

    p = 101325

    rho_ts = np.array([277.15, 283.15, 293.15, 303.15, 313.15, 323.15, 333.15])
    rho_No68 = [1000.78, 1000.55, 999.01, 996.4, 992.92, 988.70, 983.69]
    rho_No129 = [1002.04, 1001.69, 1000.17, 997.55, 994.05, 989.60, 984.6]
    rho_No27T = [1016.4, 1015.87, 1013.73, 1010.78, 1007.03, 1002.81, np.NaN]
    rho_No38T = [1017.08, 1016.05, 1014.38, 1011.43, 1007.73, 1003.45, 998.65]

    h_ts = np.array([273.2, 278.15, 283.15, 293.15, 303.15, 313.15, 323.15, 333.15])
    h_No68 = [0.0, 21.251, 42.361, 84.257, 125.87, 167.4, 209.02, 250.91]
    h_No129 = [0.0, 21.430, 42.927, 85.492, 127.82, 170.03, 212.25, 254.60]
    h_No27T = [0.0, 21.364, 42.697, 84.928, 126.96, 168.83, 210.47, 252.711]
    h_No38T = [0.0, 21.671, 43.322, 86.231, 128.82, 171.20, 192.33, 213.44]

    n = 13
    ts = np.linspace(273.2, 333.15, n)

    tppm_rho_No68 = np.zeros(n)
    tppm_rho_No129 = np.zeros(n)
    tppm_rho_No27T = np.zeros(n)
    tppm_rho_No38T = np.zeros(n)

    tppm_h_No68 = np.zeros(n)
    tppm_h_No129 = np.zeros(n)
    tppm_h_No27T = np.zeros(n)
    tppm_h_No38T = np.zeros(n)

    property = tppm.PropertyModel()

    for i, t in enumerate(ts):
        props_No68 = property.calc(fluid_No68, p, t).total.props
        props_No129 = property.calc(fluid_No129, p, t).total.props
        props_No27T = property.calc(fluid_No27T, p, t).total.props
        props_No38T = property.calc(fluid_No38T, p, t).total.props

        tppm_rho_No68[i] = props_No68.rho
        tppm_rho_No129[i] = props_No129.rho
        tppm_rho_No27T[i] = props_No27T.rho
        tppm_rho_No38T[i] = props_No38T.rho

        tppm_h_No68[i] = props_No68.h
        tppm_h_No129[i] = props_No129.h
        tppm_h_No27T[i] = props_No27T.h
        tppm_h_No38T[i] = props_No38T.h

    fig, ax1 = plt.subplots()
    ax1.plot(ts - 273.15, tppm_rho_No68, "b-", label="Sample No.68")
    ax1.plot(rho_ts - 273.15, rho_No68, "bo")
    ax1.plot(ts - 273.15, tppm_rho_No129, "g-", label="Sample No.129")
    ax1.plot(rho_ts - 273.15, rho_No129, "go")
    ax1.plot(ts - 273.15, tppm_rho_No27T, "r-", label="Sample No.27T")
    ax1.plot(rho_ts - 273.15, rho_No27T, "ro")
    ax1.plot(ts - 273.15, tppm_rho_No38T, "k-", label="Sample No.38T")
    ax1.plot(rho_ts - 273.15, rho_No38T, "ko")
    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Density, kg/m3")
    ax1.legend()
    plt.show()

    tppm_h_No68 = tppm_h_No68 - tppm_h_No68[0]
    tppm_h_No129 = tppm_h_No129 - tppm_h_No129[0]
    tppm_h_No27T = tppm_h_No27T - tppm_h_No27T[0]
    tppm_h_No38T = tppm_h_No38T - tppm_h_No38T[0]

    fig, ax1 = plt.subplots()
    ax1.plot(ts - 273.15, tppm_h_No68, "b-", label="Sample No.68")
    ax1.plot(h_ts - 273.15, h_No68, "bo")
    ax1.plot(ts - 273.15, tppm_h_No129, "g-", label="Sample No.129")
    ax1.plot(h_ts - 273.15, h_No129, "go")
    ax1.plot(ts - 273.15, tppm_h_No27T, "r-", label="Sample No.27T")
    ax1.plot(h_ts - 273.15, h_No27T, "ro")
    ax1.plot(ts - 273.15, tppm_h_No38T, "k-", label="Sample No.38T")
    ax1.plot(h_ts - 273.15, h_No38T, "ko")
    ax1.set_xlabel("Temperature, degC")
    ax1.set_ylabel("Enthalpy Change, kJ/kg")
    ax1.legend()
    plt.show()

if __name__ == "__main__":

    comp = [tppm.Comp.WATER,
            tppm.Comp.STEAM,
            tppm.Comp.Na_plus,
            tppm.Comp.Cl_minus,
            tppm.Comp.NaCl_aq,
            tppm.Comp.Halite,
            tppm.Comp.CARBONDIOXIDE,
            tppm.Comp.CO2_aq]
    masses = [1, 1e-15, 0, 0, 0, 0.1, 0.002, 0]
    tot_mass = sum(masses)
    masses = [i /tot_mass for i in masses]

    brine = tppm.Fluid(components=comp, composition=masses)

    T = 375
    P = 101325

    partition = tppm.Partition()
    partition.options.Reaktoro.speciesMode = tppm.PartitionModelOptions().Reaktoro.SpeciesMode.SELECTED
    # partition.options.Reaktoro.strictSucess = False
    brine = partition.calc(brine, P, T)

    property = tppm.PropertyModel()
    brine = property.calc(brine, P, T)

    print(brine)
