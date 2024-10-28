import time

from multiprocessing import Process, Queue, Pipe
from multiprocessing.connection import Connection

def f(reciver:Connection, sender:Connection):
    while(True):
        if not reciver.poll():
            continue

        req = reciver.recv()
        print(f"SUB :{type(req)}")

        if req == "exit":
            print("function exit")
        else:
            sender.send(req)

def get(conn:Connection):
    if not conn.poll():
        print("Main:None")
        return
    
    res = conn.recv()
    print(f"Main:{type(res)}")
    print(f"Main:{res}")

def start_multi():
    res_sender, res_reciver = Pipe()
    req_sender, req_reciver = Pipe()
    p = Process(target=f, args=(req_reciver, res_sender), daemon=True)
    p.start()

    return p, req_sender, res_reciver

if __name__ == "__main__":
    process, sender, reciver = start_multi()

    msg_str = "aaaa"
    msg_int = 1
    msg_float = 1.2
    msg_list = [1, 2, 3]
    msg_tuple = (1, 2, 3)
    msg_dict = {"a":"b"}

    # check str
    sender.send(msg_str)
    time.sleep(0.1)
    get(reciver)

    # check int
    sender.send(msg_int)
    time.sleep(0.1)
    get(reciver)

    # check float
    sender.send(msg_float)
    time.sleep(0.1)
    get(reciver)

    # check list
    sender.send(msg_list)
    time.sleep(0.1)
    get(reciver)

    # check tuple
    sender.send(msg_tuple)
    time.sleep(0.1)
    get(reciver)

    # check dict
    sender.send(msg_dict)
    time.sleep(0.1)
    get(reciver)
