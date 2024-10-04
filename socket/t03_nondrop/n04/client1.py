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
        self.socket: Optional[socket.socket] = None


    def connect(self):
        """ ソケットインスタンスを毎回作り直すようにする
        """
        try:
            family = socket.AF_INET # ipv4
            self.socket = socket.socket(family)
            self.socket.connect((self.ip_addr, self.port_num))
            return True, None
        except Exception as e:
            if isinstance(e, ConnectionRefusedError):
                ### 接続先が無い時は表示しない
                pass
            else:
                ### 想定外のエラーの時は例外を表示する
                print(type(e), e)
            self.socket = None
            return False, None


    def __send(self, msg: bytes) -> Tuple[bool, Any]:
        """ send 本体
        """
        is_success_send = False
        if isinstance(self.socket, socket.socket):
            try:
                self.socket.send(msg)
            except Exception as e:
                print(type(e), e)
                is_success_send = False
                self.socket.close()
            else:
                self.socket.shutdown(socket.SHUT_WR)
                is_success_send = True
        return is_success_send, None


    def send(self, msg: bytes) -> Tuple[bool, Any]:
        """ sendが失敗したら接続を試してもう一回sendする
        """
        is_success_send = False

        is_success_send, _ = self.__send(msg)

        if not is_success_send:
            self.connect()
            is_success_send, _ = self.__send(msg)

        return is_success_send, None


    def recv(self, buf_size: int=1024) -> Tuple[bool, Optional[bytes]]:
        is_success_recv = False
        msg: Optional[bytes] = None
        if isinstance(self.socket, socket.socket):
            try:
                msg = self.socket.recv(buf_size)
            except Exception as e:
                print(type(e), e)
                self.close()
            else:
                is_success_recv = True

        return is_success_recv, msg


    def close(self):
        is_success_close = False
        if isinstance(self.socket, socket.socket):
            try:
                self.socket.close()
                self.socket = None
            except Exception as e:
                print(type(e), e)
            else:
                is_success_close = True
        return is_success_close


if __name__ == "__main__":
    # クライアント側から接続依頼
    loop_count = 0
    cs = CustomSocket()
    while(True):
        time.sleep(0.3)
        is_success, _ = cs.connect()
        print("Connection:", is_success)
        if not is_success:
            continue

        # データの送信
        data_dict = {}
        data_dict['command'] = 'process'
        data_dict['text'] = "ab"*250 + "cd"*250 + "ef"*250
        print(f"SendData:{data_dict}")
        text = json.dumps(data_dict)
        msg: bytes = text.encode()
        is_success, _ = cs.send(msg)
        print(f"Send Success:{is_success}")
        if not is_success:
            continue

        # データの受信
        bufsize = 1024
        is_success, recv_msg = cs.recv()
        print(f"Recv Success:{is_success}")
        if not is_success:
            continue
        if not isinstance(recv_msg, bytes):
            continue
        recv_text: str = recv_msg.decode()
        print(f"RecvData:{recv_text}")

        time.sleep(2)

        # データの送信
        data_dict = {}
        data_dict['command'] = 'process'
        data_dict['text'] = "ab"*250 + "cd"*250 + "ef"*250
        print(f"SendData:{data_dict}")
        text = json.dumps(data_dict)
        msg: bytes = text.encode()
        is_success, _ = cs.send(msg)
        print(f"Send Success:{is_success}")
        if not is_success:
            continue

        # データの受信
        bufsize = 1024
        is_success, recv_msg = cs.recv()
        print(f"Recv Success:{is_success}")
        if not is_success:
            continue
        if not isinstance(recv_msg, bytes):
            continue
        recv_text: str = recv_msg.decode()
        print(f"RecvData:{recv_text}")

        break