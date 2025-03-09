import pprint

class A:
    def __init__(self, *args, **kwargs):
        self.x = 1
        self.y = 2


    def func(self, *args, **kwargs):
        pprint.pprint(locals())



if __name__ == "__main__":
    a = A()
    a.func()

