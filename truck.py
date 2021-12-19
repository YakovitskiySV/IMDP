"""track class module"""

from vechicles import VechicleType as vt
from env import *

class Truck:
    """truck class"""
    def __init__(self, truck_type):
        self.__type = truck_type

    def get_type(self):
        """get this truck type"""
        return self.__type

    def __str__(self):
        return f"truck with type {self.__type}"
