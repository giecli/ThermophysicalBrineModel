import ThemophysicalPropertyModel as tppm
import pickle
import time

# Maasland: MLD-GT-01-S1
if __name__ == "__main__":

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










