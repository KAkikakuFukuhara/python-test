""" setterの書き方:setterとは代入できるようにする機能
"""
class Hoge:
    def __init__(self, value: int):
        self.__x: int = value


    @property
    def x(self) -> int:
        return self.__x


    @x.setter
    def x(self, value: int):
        self.__x = value


if __name__ == "__main__":
    hoge = Hoge(1)
    print("x=", hoge.x)
    hoge.x = 2 # Error
    print("x=", hoge.x)
