"""vechicle classes used in factory"""
from enum import Enum
from state import State
from env import *


class Vechicle:
    """vechicle class"""

    def __init__(self, v_type):
        self.type = v_type
        self.__free_at = 0
        self.__state = State.FREE

    def __str__(self):
        return str(self.type).split(".")[1]

    def get_state(self, current_time):
        self.check_busy(current_time)
        return self.__state

    def set_busy(self, busy_time, current_time):
        assert self.__state == State.FREE
        self.__free_at = current_time + busy_time
        self.__state = State.BUSY

    def check_busy(self, current_time):
        if self.__free_at < current_time:
            self.__state = State.FREE


if __name__ == "__main__":
    v1 = Vechicle(VechicleType.V_LOADER)
    v2 = Vechicle(VechicleType.CRANE)
    print(v1)
    print(v2)
