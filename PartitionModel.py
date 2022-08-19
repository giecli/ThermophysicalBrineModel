from UserEnteredPartitionModel import UserPartition, UserPartitionOptions
from ReaktoroPartitionModel import ReaktoroPartition, ReaktoroPartitionOptions

from enum import Enum


class PartitionModelOptions:
    UserEntered = UserPartitionOptions()
    Reaktor = ReaktoroPartitionOptions()


class PartitionModels(Enum):
    USER_ENTERED = UserPartition
    REAKTORO = ReaktoroPartition


class Partition:

    def __init__(self, model=PartitionModels.REAKTORO, options=PartitionModelOptions()):

        self.partitionModel = model
        self.options = options

    def calc(self, fluid, P, T):

        return self.partitionModel.value.calc(fluid, P, T, self.options)
