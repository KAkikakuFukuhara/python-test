from multiprocessing import Process, Queue, Pipe
from multiprocessing.connection import Connection

def f(reciver:Connection, sender:Connection):
    while(True):
        if not reciver.poll():
            continue

        req = reciver.recv()
        print(type(req))
        req = str(req)

        if req == "exit":
            print("function exit")
        else:
            sender.send(req)

def get(conn:Connection):
    if not conn.poll():
        print("None")
        return
    
    res = conn.recv()
    print(type(res))
    print(res)

def start_multi():
    res_sender, res_reciver = Pipe()
    req_sender, req_reciver = Pipe()
    p = Process(target=f, args=(req_reciver, res_sender), daemon=True)
    p.start()

    return p, req_sender, res_reciver

if __name__ == "__main__":
    process, sender, reciver = start_multi()


