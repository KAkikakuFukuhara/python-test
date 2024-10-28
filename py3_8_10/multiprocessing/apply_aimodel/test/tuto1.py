"""
    マルチプロセッシング入門：
    関数と引数を渡してマルチプロセスを実行する.
"""
from multiprocessing import Process
from time import sleep

# main
def func_1(num):
    print("Start:main process")
    for i in range(num):
        print(f"main process:{i}")
        sleep(1)
    else:
        print("End:main process")

def func_2(num, name):
    print(f"Start:sub {name} process")
    for i in range(num):
        print(f"sub {name} process:{i}")
        sleep(1)
    else:
        print(f"End:sub {name} process")

if __name__ == "__main__":
    p = Process(target=func_2, args=(10, "alfa"))
    q = Process(target=func_2, args=(10, "beta"))
    p.start()
    q.start()
    func_1(10)
