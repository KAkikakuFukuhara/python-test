import multiprocessing
import time

def func():
    start = time.time()
    i = 0
    while True:
        print(i)
        i += 1
        time.sleep(1)
        elapsed_time = time.time() - start
        if elapsed_time > 180:
            break
    
def main():
    process = multiprocessing.Process(target=func, daemon=True)

    process.start()
    
    time.sleep(10)

if __name__ == '__main__':
    main()

