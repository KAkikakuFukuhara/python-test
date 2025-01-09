""" インターフェースを用いたタイプヒント
"""
from abc import ABC, abstractmethod


class InterfaceA(ABC):
    @abstractmethod
    def a(self):
        pass


class InterfaceB(ABC):
    @abstractmethod
    def b(self):
        pass


class A(InterfaceA):
    def a(self):
        print("a")


class A2(InterfaceA):
    def a(self):
        print("a2")


class B(InterfaceB):
    def b(self):
        print("b")


def execute(x: InterfaceA):
    x.a()


a = A()
a2 = A2()
b = B()

execute(a)
execute(a2)
execute(b) ## 失敗する
