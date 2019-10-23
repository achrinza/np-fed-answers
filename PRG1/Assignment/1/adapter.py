from abc import ABC
from abc import abstractmethod

class Adapter(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def call(self):
        raise NotImplementedError
