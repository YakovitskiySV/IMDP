"""main func file"""
from gui import create_window
import column as cl
from factory import Factory
from env import *
import random


if __name__ == "__main__":
    fac = Factory()
    current_time = 0
    new_column = cl.TruckColumn()
    next_column_time = random.expovariate(1 / NEXT_COLUMN_K)
    while current_time != STOP_TIME:
        if next_column_time < current_time:
            new_column = cl.TruckColumn()
            fac.add_trucks(new_column.get_trucks())
            fac.unload_trucks(current_time)
            next_column_time = random.expovariate(1 / NEXT_COLUMN_K)
            print(current_time)
        current_time += 1
