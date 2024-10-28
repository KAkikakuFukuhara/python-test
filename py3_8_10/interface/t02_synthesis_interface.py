""" インターフェースの合成
"""
from abc import abstractmethod, ABC


class A(ABC):
    @abstractmethod
    def a(self):
        pass


class B(ABC):
    @abstractmethod
    def b(self):
        pass

### インターフェースの合成
class C(A, B):
    pass


class ConcreateA(A):
    def a(self):
        print("a_a")


class ConcreateB(B):
    def b(self):
        print("b_b")


class ConcreateC(C):
    def a(self):
        print("c_a")


    def b(self):
        print("c_b")


class D(A, B):
    ### 実質的にCと変わらないはず
    def a(self):
        print("d_a")


    def b(self):
        print("d_b")


def func1(x: A):
    x.a()


def func2(x: B):
    x.b()


def func3(x: C):
    x.a()
    x.b()


if __name__ == "__main__":

    w = ConcreateA()
    x = ConcreateB()
    y = ConcreateC()
    z = D()

    func1(w)
    # func1(x) # 実行できない
    func1(y)
    func1(z)

    # func2(w) # 実行できない
    func2(x)
    func2(y)
    func2(z)

    # func3(w) # 実行できない
    # func3(x) # 実行できない
    func3(y)
    func3(z) # 実行できるがVSCode上ではエラー表記

