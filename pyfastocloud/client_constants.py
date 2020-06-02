from enum import IntEnum

RequestReturn = (bool, str)

class ClientStatus(IntEnum):
    INIT = 0
    CONNECTED = 1
    ACTIVE = 2
