from enum import Enum


STOP_TIME = 44_640  # minutes in one month
NEXT_COLUMN_K = 540  # minutes

PLATFORM_NUMBER = 10
V_LOADERS_NUMBER = 8
CRANES_NUMBER = 2

STD_DEVIATION = 3
MATHEMATICAL_EXPECTATION = 14

LOW_TRIG = 4
HIGH_TRIG = 10
MODE_TRIG = 8


class VechicleType(Enum):
    """types of vechicles used in factory"""

    V_LOADER = 1
    CRANE = 2


TRUCK_TYPES = {  # with unload time
    1: 22,
    2: 21,
    3: 27,
    4: 24,
    5: 17,
    6: 19,
    7: 22,
    8: 31,
    9: 28,
    10: 29,
}

TRUCK_VECH_TYPES = {
    1: VechicleType.V_LOADER,
    2: VechicleType.V_LOADER,
    3: VechicleType.V_LOADER,
    4: VechicleType.V_LOADER,
    5: VechicleType.V_LOADER,
    6: VechicleType.V_LOADER,
    7: VechicleType.V_LOADER,
    8: VechicleType.CRANE,
    9: VechicleType.CRANE,
    10: VechicleType.CRANE,
}
