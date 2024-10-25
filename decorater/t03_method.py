""" インスタンスのメソッドに対してデコレータを適用する
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print("decorator")
        func(*args, **kwargs)
    return wrapper


class Test:
    @decorator
    def method(self, x):
        print(x)

test = Test()
test.method(1)
