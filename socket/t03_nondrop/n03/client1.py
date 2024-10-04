""" 通信先でJsonで受け取るはずなのにJsonで送らない：エラーは発生しないが
"""
import socket
import json


class CustomSocket:
    def __init__(self, socket_: socket.socket):
        self.ip_addr: str = "127.0.0.1"
        self.port_num: int = 50001
        self.socket = socket_


    def connect(self):
        self.socket.connect((self.ip_addr, self.port_num))


    def send(self, msg: bytes):
        try:
            self.socket.send(msg)
            self.socket.shutdown(socket.SHUT_WR)
        except Exception as e:
            print(e)


    def recv(self):
        bufsize = 1024
        try:
            recv_msg = self.socket.recv(bufsize)
        except Exception as e:
            print(e)
            recv_msg = b''
        return recv_msg


if __name__ == "__main__":
    # 通信部分（ソケット）の準備
    family = socket.AF_INET # ipv4
    socket_ = socket.socket(family)

    # クライアント側から接続依頼
    cs = CustomSocket(socket_)
    cs.connect()

    # データの送信
    text = "aaaa"
    print(f"Send:{text}")
    msg: bytes = text.encode()
    cs.send(msg)

    # データの受信
    bufsize = 1024
    recv_msg = cs.recv()
    recv_text: str = recv_msg.decode()
    print(f"Recv:{recv_text}")
