"""platform class"""
from state import State
import random
import datetime as dt
from env import *


def gen_p_id():
    x = 0
    while True:
        x += 1
        yield x


class Platform:
    """platform class"""

    def __init__(self):
        self.__state = State.FREE
        self.__free_at = 0
        self.__vech = None

    def unload_truck(self, truck, vech, current_time):
        assert self.__state == State.FREE
        self.__state = State.BUSY
        self.__vech = vech
        busy_time = Platform.__calculate_unload_time(truck)
        self.__free_at = current_time + busy_time
        self.__vech.set_busy(busy_time, current_time)
        self.print_stat(busy_time)

    def print_stat(self, busy_time):
        print(f"plat {id(self)} busy for {busy_time}")

    @staticmethod
    def __calculate_unload_time(truck):
        return random.expovariate(1 / TRUCK_TYPES[truck.get_type()])

    def get_state(self, current_time):
        self.__check_busy(current_time)
        return self.__state

    def __check_busy(self, current_time):
        if self.__free_at < current_time:
            self.__state = State.FREE
            if self.__vech is not None:
                self.__vech.check_busy(current_time)
