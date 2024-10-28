""" 落ちていたら自動再接続
"""
from typing import Optional, Tuple, Any
import socket
import json
import time


class CustomSocket:
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


    def __send(self, msg: bytes):
        """ send 本体
        """
        self.socket.send(msg)
        self.socket.shutdown(socket.SHUT_WR)


    def send(self, msg: bytes):
        """ sendが失敗したら接続を試してもう一回sendする
        """
        try:
            self.__send(msg)
        except Exception as e:
            self.connect()
            self.__send(msg)


    def recv(self, buf_size: int=1024) -> bytes:
        msg = self.socket.recv(buf_size)
        return msg


    def close(self):
        self.socket.close()


if __name__ == "__main__":
    # クライアント側から接続依頼
    loop_count = 0
    cs = CustomSocket()
    while(True):
        time.sleep(0.3)
        try:
            cs.connect()
            print("Connection Success")
        except Exception as e:
            continue

        # データの送信
        data_dict = {}
        data_dict['command'] = 'process'
        data_dict['text'] = "ab"*250 + "cd"*250 + "ef"*250
        print(f"SendData:{data_dict}")
        text = json.dumps(data_dict)
        msg: bytes = text.encode()
        try:
            cs.send(msg)
            print(f"Send Success")
        except Exception as e:
            continue

        # データの受信
        try:
            recv_msg = cs.recv()
            print(f"Recv Success")
        except Exception as e:
            continue
        recv_text: str = recv_msg.decode()
        print(f"RecvData:{recv_text}")

        time.sleep(3)

        # データの送信
        data_dict = {}
        data_dict['command'] = 'process'
        data_dict['text'] = "ab"*250 + "cd"*250 + "ef"*250
        print(f"SendData:{data_dict}")
        text = json.dumps(data_dict)
        msg: bytes = text.encode()
        try:
            cs.send(msg)
        except Exception as e:
            continue
        print(f"Send Success")

        # データの受信
        bufsize = 1024
        try:
            recv_msg = cs.recv()
        except Exception as e:
            continue
        print(f"Recv Success")
        recv_text: str = recv_msg.decode()
        print(f"RecvData:{recv_text}")

        break