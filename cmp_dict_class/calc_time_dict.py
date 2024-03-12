import time


def calc_time(x:dict):
    start_time = time.time()
    for i in range(1000000):
        y = x.copy()

    elapd_time = time.time() - start_time
    print(elapd_time)

if __name__ == "__main__":
    x = {"a":1}
    calc_time(x)