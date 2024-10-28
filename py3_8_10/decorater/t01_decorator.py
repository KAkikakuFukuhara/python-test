
def add(x, y):
    return x + y


def print_func(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print("in-decorator", arg)
        for k, v in kwargs.items():
            print("in-decorator", f"{k}={v}")
        res = func(*args, **kwargs)
        print("in-decorator", f"res={res}")
        return res
    return wrapper


@print_func
def add2(x: int, y: int):
    return x + y


if __name__ == "__main__":
    x = 1; y = 2
    print(add(x, y))
    print(add2(x, y))
    print(add2(x=x, y=y))