""" 抽象メソッドとpropetryの組み合わせの書き方
"""
from abc import ABC, abstractmethod


class IHoge(ABC):
    @property
    @abstractmethod
    def x(self) -> int:
        pass


    @x.setter
    @abstractmethod
    def x(self, value: int):
        pass


class Hoge1(IHoge):
    def __init__(self, value: int):
        self.__x: int = value


    @property
    def x(self) -> int:
        return self.__x


    @x.setter
    def x(self, value: int):
        self.__x = value


class Hoge2(IHoge):
    def __init__(self, value: int):
        self.__x: int = value


    @property
    def x(self) -> int:
        return self.__x


    ### setterが実装されていないのにvscodeが注意してくれない
    # @x.setter
    # def x(self, value: int):
    #     self.__x = value


class Hoge3(IHoge):
    def __init__(self, value: int):
        self.__x: int = value


    def x(self) -> int:
        """ vscodeがpropetryじゃないのに問題を教えてくれない
        """
        return self.__x



if __name__ == "__main__":
    hoge = Hoge1(1)
    print("x=", hoge.x)
    hoge.x = 11

    hoge2 = Hoge2(2)
    print("x=", hoge2.x)
    try:
        hoge2.x = 3
    except Exception as e:
        print(type(e), e)

    hoge3 = Hoge3(3)
    print("x=", hoge3.x) # 関数扱い
