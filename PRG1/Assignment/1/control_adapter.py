from abc import ABC
from abc import abstractmethod
from adapter import Adapter

class ControlAdapterCalls:
    def __init__(self):
        pass

    get_userinput_directional = "GET_USERINPUT_DIRECTIONAL"
    get_userinput_string = "GET_USERINPUT_STRING"

class ControlAdapterUserInputDirectionals:
    def __init__(self):
        pass

    up = "UP"
    down = "DOWN"
    left = "LEFT"
    right = "RIGHT"

class ControlAdapter(Adapter, ABC):
    ADAPTER_TYPE = "ControlAdapter"

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def call(self):
        raise NotImplementedError

    @abstractmethod
    def _get_userinput_directional(self):
        raise NotImplementedError

    @abstractmethod
    def _get_userinput_string(self):
        raise NotImplementedError
