""" デコレータに引数を渡す方法
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print(func)
        func(*args, **kwargs)
    return wrapper


@decorator
def f1(x):
    print(x)


### デコレータのクロージャーを作成する
def decorator2(pre_print: str):
    def decorator3(func):
        def wrapper(*args, **kwargs):
            print(pre_print)
            print(func)
            func(*args, **kwargs)
        return wrapper
    return decorator3


@decorator2(pre_print="hello")
def f2(x):
    print(x)


if __name__ == "__main__":
    f1("test")
    f2("test2")
