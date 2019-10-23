from abc import ABC
from abc import abstractmethod
from adapter import Adapter

class DisplayAdapterCalls:
    clear = "CLEAR"
    show_text = "SHOW_TEXT"
    show_maze = "SHOW_MAZE"

class DisplayAdapter(Adapter, ABC):
    ADAPTER_TYPE = "DisplayAdapter"
    
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def call(self):
        raise NotImplementedError

    @abstractmethod
    def _clear(self):
        raise NotImplementedError

    @abstractmethod
    def _show_text(self):
        raise NotImplementedError

    @abstractmethod
    def _show_maze(self):
        raise NotImplementedError
