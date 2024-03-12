from threading import Thread
from multiprocessing import Process
from queue import Queue as th_Queue
from multiprocessing import Queue as ps_Queue
import time

def count_process(state_queue:ps_Queue, result_queue:ps_Queue):
    j = 0
    while(True):
        if not state_queue.empty():
            state = state_queue.get()
            if state == "exit":
                result_queue.put(j)
                break
        print(f"\rcount:{j:8}", end="")
        j += 1
    print("")

def count_thread(state_queue:th_Queue, result_queue:th_Queue):
    j = 0
    while(True):
        if not state_queue.empty():
            state = state_queue.get()
            if state == "exit":
                result_queue.put(j)
                break
        print(f"\rcount:{j:8}", end="")
        j += 1
    print("")

def test_process():
    limit_time = 5
    state_queue = ps_Queue()
    result_queue = ps_Queue()
    ps = Process(target=count_process, args=(state_queue, result_queue), daemon=True)
    start_time = time.time()
    ps.start()
    while(True):
        elapdtime = time.time() - start_time
        if elapdtime > limit_time:
            break
    state_queue.put("exit")
    ps.join()
    res = result_queue.get()

def test_thread():
    limit_time = 5
    state_queue = th_Queue()
    result_queue = th_Queue()
    th = Thread(target=count_thread,  args=(state_queue, result_queue), daemon=True)
    start_time = time.time()
    th.start()
    while(True):
        elapdtime = time.time() - start_time
        if elapdtime > limit_time:
            break
    state_queue.put("exit")
    th.join()
    res = result_queue.get()

def main():
    print("5秒間ループを回してインクリメントするプログラム")
    print("マルチスレッドの場合")
    test_thread()
    print("マルチプロセスの場合")
    test_process()

if __name__ == "__main__":
    main()    