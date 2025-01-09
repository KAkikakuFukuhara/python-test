""" 特殊メソッドをインターフェースで指定できるか？：結論＝できる

    特殊メソッドとは：
        クラスの関数である__repr__や__getitem__などのこと
"""
from abc import ABC, abstractmethod
from typing import Any


class IHoge(ABC):
    @abstractmethod
    def __getitem__(self, value: int) -> Any:
        pass


class FailureExampleHoge(IHoge):
    def __init__(self):
        self.items = list(range(5))


class SuccessExampleHoge(IHoge):
    def __init__(self):
        self.items = list(range(5))


    def __getitem__(self, value: int) -> Any:
        return self.items[value]


def failure_example():
    try:
        hoge = FailureExampleHoge()
    except Exception as e:
        print(type(e), e)
    else:
        print("hoge[0]=", hoge[0])


def success_example():
    try:
        hoge = SuccessExampleHoge()
    except Exception as e:
        print(type(e), e)
    else:
        print("hoge[0]=", hoge[0])


if __name__ == "__main__":
    failure_example()
    success_example()
