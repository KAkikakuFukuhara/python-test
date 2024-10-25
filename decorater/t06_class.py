""" classでデコレータを作成する
"""

class Decorator:
    def __init__(self):
        self.x = "decorate"


    def decorate(self, func):
        def wrapper(*args, **kwargs):
            print(self.x)
            res = func(*args, **kwargs)
            return res
        return wrapper


decorator = Decorator()
@decorator.decorate
def func2(x1, x2):
    print(x1 + x2)


func2(1, 2)
