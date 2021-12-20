"""factory class"""
from platforms import Platform
import vechicles as vech

from state import State
from env import *


class Factory:
    """class for modeling a factory"""

    def __init__(self):
        self.__trucks = []
        x = Platform()
        self.__platforms = [Platform() for _ in range(PLATFORM_NUMBER)]
        v_loaders = [
            vech.Vechicle(vech.VechicleType.V_LOADER) for _ in range(V_LOADERS_NUMBER)
        ]
        cranes = [vech.Vechicle(vech.VechicleType.CRANE) for _ in range(CRANES_NUMBER)]
        self.__vechicles = v_loaders + cranes

    def add_trucks(self, trucks: list):
        """add trucks to dock"""
        self.__trucks.extend(trucks)

    def unload_trucks(self, current_time: int):
        """start unloading truck"""
        if not self.__trucks:
            return None
        for i, truck in enumerate(self.__trucks):
            free_platform, free_vech = self.__find_free_plat_and_vech(
                truck, current_time
            )
            if free_platform is None:
                print("unable to unload: no free platform")
                return
            if free_vech is not None:
                free_platform.unload_truck(truck, free_vech, current_time)
                print(f"unloading: {truck} with {free_vech}")
                self.__trucks.pop(i)
            else:
                print("unable to unload: no free vechihle")

        print(f"trucks queue: {len(self.__trucks)}")

    def __find_free_plat_and_vech(self, truck, current_time):
        if not self.__trucks:
            return (None, None)

        free_platform = None
        for platform in self.__platforms:
            if platform.get_state(current_time) == State.FREE:
                free_platform = platform
                break

        free_vech = None
        for vech in self.__vechicles:
            if (
                vech.get_state(current_time) == State.FREE
                and vech.type == TRUCK_VECH_TYPES[truck.get_type()]
            ):
                free_vech = vech
                break

        return (free_platform, free_vech)
