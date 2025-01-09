from typing import Literal


def func(x: Literal['a', 'b', 'c']):
    return x


### success
func('a')
func('b')
func('c')
### failure
func(list('abc')[0])
