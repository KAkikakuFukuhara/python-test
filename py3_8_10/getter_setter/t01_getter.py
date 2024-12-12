""" getterの書き方:getterとは代入できない参照だけできる仕組み
"""
class Hoge:
    def __init__(self, x: int):
        self.__x: int = x


    @property
    def x(self) -> int:
        return self.__x


if __name__ == "__main__":
    hoge = Hoge(1)
    print("x=", hoge.x)
    hoge.x = 2 # 値の代入はできない
