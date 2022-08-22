from UserEnteredPartitionModel import UserPartition, UserPartitionOptions
from ReaktoroPartitionModel import ReaktoroPartition, ReaktoroPartitionOptions

from enum import Enum


class PartitionModelOptions:

    class PartitionModels(Enum):
        USER_ENTERED = UserPartition
        REAKTORO = ReaktoroPartition

    def __init__(self):
        self.model = self.PartitionModels.REAKTORO

        self.UserEntered = UserPartitionOptions()
        self.Reaktoro = ReaktoroPartitionOptions()


class Partition:

    def __init__(self, options=PartitionModelOptions()):

        self.options = options
        self.partitionModel = options.model

    def calc(self, fluid, P, T):

        fluid.total.props_calculated = False
        fluid.aqueous.props_calculated = False
        fluid.gaseous.props_calculated = False
        fluid.mineral.props_calculated = False

        return self.partitionModel.value.calc(fluid, P, T, self.options)
