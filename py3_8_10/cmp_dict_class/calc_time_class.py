import time
import copy

class A:
    def __init__(self):
        self.a = 1

def calc_time(x:A):
    start_time = time.time()
    for i in range(1000000):
        y = copy.copy(x)

    elapd_time = time.time() - start_time
    print(elapd_time)

if __name__ == "__main__":
    x = A()
    calc_time(x)