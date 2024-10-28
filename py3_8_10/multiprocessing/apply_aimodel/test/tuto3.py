import multiprocessing, time
import numpy as np
 
def func(arg_queue):
    arg_queue.put(1)
    time.sleep(2.0)
    arg_queue.put(2)
    time.sleep(2.0)
    arg_queue.put(3)
    time.sleep(2.0)
    arg_queue.put(None)
 
def main():
    #キューの生成
    queue = multiprocessing.Queue()
    #プロセスの生成
    process = multiprocessing.Process(target=func, args=(queue,))
 
    #プロセス開始
    process.start()
 
    while(True):
        if queue.empty():
            continue
        try:
            #待ち
            s = queue.get(True, 5)   #キューに入るまで待ち。timeout 5秒
            if s==None : break
            print(s)
        except:
            break
 
    process.join()
    print('finish')
 
def main2():
    # キューの作成
    queue = multiprocessing.Queue()
    if queue.empty():
        return "None"
    else:
        return queue.get(True, 1)

if __name__ == '__main__':
    main()
    time.sleep(5)