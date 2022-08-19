import copy


class UserPartitionOptions:

    pass


class UserPartition:

    @staticmethod
    def calc(fluid, P, T, options):
        print("User Partition")
        return copy.deepcopy(fluid)
