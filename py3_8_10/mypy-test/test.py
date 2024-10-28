from typing import Type

class A:
    def __init__(self, x:int):
        self.x = 1

    def print(self):
        print(self.x)

class B(A):
    def __init__(self, x:int):
        self.x = x + 1

    def test(self):
        print(self.x)

a = A(1)
b = B(1)
c = A("a") # error

def test(cls:A):
    cls.print()

test(a)
test(b)
