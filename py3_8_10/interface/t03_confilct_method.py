from abc import ABC, abstractmethod


class InterfaceA(ABC):
    @abstractmethod
    def print(self):
        pass


class InterfaceB(ABC):
    @abstractmethod
    def print(self):
        pass


class C(InterfaceA, InterfaceB):
    def print(self):
        print("C")


