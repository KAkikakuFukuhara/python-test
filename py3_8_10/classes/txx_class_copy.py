from __future__ import annotations
import copy
import random


class MyClass:
    def __init__(self):
        self.x: int = random.randint(0, 10)
        self.y_list1: list = [ random.randint(0, 10) for _ in range(5)]
        self.y_list2: list = [ random.randint(0, 10) for _ in range(5)]


    def reset(self):
        self.x = random.randint(10, 20)
        self.y_list1: list = [ random.randint(0, 10) for _ in range(5)]
        for idx in range(len(self.y_list2)):
            self.y_list2[idx] = random.randint(0, 10)


    def print_elem(self):
        print(self.x, self.y_list1, self.y_list2)


myclass = MyClass()
myclass2 = copy.copy(myclass)
myclass3 = copy.deepcopy(myclass)

print(id(myclass), end=": ")
myclass.print_elem()

print("reset")
myclass.reset()

print(id(myclass), end=": ")
myclass.print_elem()
print(id(myclass2), end=": ")
myclass2.print_elem()
print(id(myclass3), end=": ")
myclass3.print_elem()
