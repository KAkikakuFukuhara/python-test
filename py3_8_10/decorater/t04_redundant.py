""" 複数のデコレータを適用する
"""
def deco1(func):
    def wrapper(*args, **kwargs):
        print("deco1")
        func(*args, **kwargs)
    return wrapper


def deco2(func):
    def wrapper(*args, **kwargs):
        print("deco2")
        func(*args, **kwargs)
    return wrapper


@deco1
@deco2
def func(x):
    print(x)


class Test:
    @deco1
    @deco2
    def func(self, x):
        print(x)


if __name__ == "__main__":
    func(1)
    t = Test()
    t.func(1)
