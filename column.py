"""trucks column class"""
import random
import truck
from env import *


class TruckColumn:
    """column of trucks class"""

    def __init__(self):
        random.seed()
        self.__trucks_number = random.randint(
            MATHEMATICAL_EXPECTATION - STD_DEVIATION,
            MATHEMATICAL_EXPECTATION + STD_DEVIATION,
        )
        self.__truck_types = TruckColumn.__generate_truck_types()
        self.__trucks = [truck.Truck(truck_type) for truck_type in self.__truck_types]

        for i in range(self.__trucks_number - len(self.__trucks)):
            self.__trucks.append(truck.Truck(random.choice(self.__truck_types)))
        self.__validate_column()

    def get_trucks(self) -> list:
        """get all trucks in this column"""
        return self.__trucks

    @staticmethod
    def __generate_truck_types() -> list:
        """generate list of truck types"""
        truck_types_number = int(
            random.triangular(low=LOW_TRIG, high=HIGH_TRIG, mode=MODE_TRIG)
        )
        column_truck_types = []
        while len(column_truck_types) != truck_types_number:
            cur_type = random.choice([x for x in truck.TRUCK_TYPES.keys()])
            if cur_type not in column_truck_types:
                column_truck_types.append(cur_type)
        return column_truck_types

    def __str__(self):
        msg = f"trucks in column: {len(self.__trucks)}"
        for i, truck in enumerate(self.__trucks):
            msg += f"\t\n{i}: {truck}"
        return msg

    def __validate_column(self):
        """validate generated column"""
        assert self.__trucks_number == len(self.__trucks)
        used_truck_types = set()
        for truck in self.__trucks:
            truck_type = truck.get_type()
            assert truck_type in self.__truck_types
            used_truck_types.add(truck_type)
        assert sorted(self.__truck_types) == sorted(used_truck_types)


# test

if __name__ == "__main__":
    column = TruckColumn()
    print(column)
