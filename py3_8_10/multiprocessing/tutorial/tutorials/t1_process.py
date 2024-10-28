import time
from multiprocessing import Process

# 並列処理させる関数
def nijou(x):
    print('input: %d' % x)
    time.sleep(x)
    retValue = x * x
    print('double: %d' % (retValue))
    return(retValue)


if __name__ == "__main__":
    p1 = Process(target=nijou, args=(3,))
    p2 = Process(target=nijou, args=(2,))

    p1.start()
    p2.start()
    print("Process started.")
    p1.join()
    p2.join()
    print("process joined. ")