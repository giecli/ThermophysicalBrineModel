from Phases import *
from Components import Comp
from ErrorHandling import Error, InputError


class Fluid:

    def __init__(self, components, composition):

        # check that same number of components and compositions have been entered
        if len(components) != len(composition):
            raise InputError("\n\nThe number of components and compositions provided is not the same")

        # check that all components exist within the database
        bad_components = [comp for comp in components if type(comp) != Comp]
        if bad_components:
            message = "\n\nThe following components do not exist in the database:\n"
            for comp in bad_components:
                message = message + "\t{}\n".format(comp)
            message = message + "\nPlease check spelling or add components to the database"

            raise InputError(message)

        # check that all compositions have been entered in the right format
        bad_composition = [components[i] for i in range(len(composition)) if type(composition[i]) not in [int, float]]
        if bad_composition:
            message = "\n\nThe following composition(s) are incorrectly formatted (int or float expected):\n"
            for comp in bad_composition:
                message = message + "\t{}\n".format(comp)
            message = message + "\nPlease check input compositions"

            raise InputError(message)

        # the components and compositions are valid, now add them to the respective phases
        self.total = TotalPhase()
        self.aqueous = AqueousPhase()
        self.liquid = LiquidPhase()
        self.gaseous = GaseousPhase()
        self.mineral = MineralPhase()

        charge = 0
        for i in range(len(components)):
            comp = components[i]
            mass = composition[i]
            moles = mass / comp.value.Mr
            phase = comp.value.phase

            # add the component to the respective phase
            self.total.add_component(comp, mass, moles, update=False)
            if phase == PhaseType.AQUEOUS:
                self.aqueous.add_component(comp, mass, moles, update=False)
                self.total.phases[PhaseType.AQUEOUS] = self.aqueous
            elif phase == PhaseType.LIQUID:
                self.liquid.add_component(comp, mass, moles, update=False)
                self.total.phases[PhaseType.liquid] = self.liquid
            elif phase == PhaseType.GASEOUS:
                self.gaseous.add_component(comp, mass, moles, update=False)
                self.total.phases[PhaseType.GASEOUS] = self.gaseous
            elif phase == PhaseType.MINERAL:
                self.mineral.add_component(comp, mass, moles, update=False)
                self.total.phases[PhaseType.MINERAL] = self.mineral

            # update the total charge imbalance
            charge += moles * comp.value.charge

        # re-calculte the component mass and mole fractions
        self.total.update()
        self.liquid.update()
        self.aqueous.update()
        self.gaseous.update()
        self.mineral.update()

        if abs(charge) > 1e-3:
            raise InputError("\n\nThe fluid is not charge balanced. The charge imbalance is {}".format(charge))

    def promotePhaseToFluid(self, phase):
        # TODO
        pass

    def addComponent(self, component, composition):
        # TODO
        pass

    def addComponents(self, components, composition):
        # TODO
        pass

    @staticmethod
    def blendFluids(fluid):
        # TODO
        pass

    # TODO something to print the Fluid, underlying phases and properties
