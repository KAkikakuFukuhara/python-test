""" 落ちていたら自動再接続
"""
import socket
import json

from client3_2 import CustomSocket

class CustomSocket2(CustomSocket):
    def __init__(self):
        self.ip_addr: str = "127.0.0.1"
        self.port_num: int = 50001
        self.socket: socket.socket


    def connect(self):
        """ ソケットインスタンスを毎回作り直すようにする
        """
        family = socket.AF_INET # ipv4
        self.socket = socket.socket(family)
        self.socket.connect((self.ip_addr, self.port_num))


    def send(self, msg: bytes):
        try:
            self.socket.send(msg)
            self.socket.shutdown(socket.SHUT_WR)
        except Exception as e:
            self.connect() # 落ちていたら
            self.send(msg)


if __name__ == "__main__":
    # クライアント側から接続依頼
    cs = CustomSocket2()
    cs.connect()

    # データの送信
    data_dict = {}
    data_dict['command'] = 'process'
    data_dict['text'] = "ab"*250 + "cd"*250 + "ef"*250
    print(f"Send:{data_dict}")
    text = json.dumps(data_dict)
    msg: bytes = text.encode()
    cs.send(msg)

    # データの受信
    bufsize = 1024
    recv_msg = cs.recv()
    recv_text: str = recv_msg.decode()
    print(f"Recv:{recv_text}")

    # データの送信
    data_dict = {}
    data_dict['command'] = 'process'
    data_dict['text'] = "ab"*250 + "cd"*250 + "ef"*250
    print(f"Send:{data_dict}")
    text = json.dumps(data_dict)
    msg: bytes = text.encode()
    cs.send(msg)

    # データの受信
    bufsize = 1024
    recv_msg = cs.recv()
    recv_text: str = recv_msg.decode()
    print(f"Recv:{recv_text}")
