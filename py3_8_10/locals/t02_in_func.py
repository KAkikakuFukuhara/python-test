"""関数内部でのlocals
"""
import pprint


def func(*args, **kwargs):
    y = 2
    pprint.pprint(locals())



if __name__ == "__main__":
    x = 1
    func()
