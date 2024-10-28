import socket
import time

if __name__ == "__main__":
    # 通信部分（ソケット）の準備
    family = socket.AF_INET # ipv4
    socket_ = socket.socket(family)

    # クライアント側から接続依頼
    ip_addr: str = "127.0.0.1"
    port_num: int = 50001
    try:
        socket_.connect((ip_addr, port_num))
    except ConnectionRefusedError as e:
        print(e)

    # データの受信
    bufsize = 1024
    recv_msg: bytes = socket_.recv(bufsize)
    recv_text: str = recv_msg.decode()
    print(f"Recv:{recv_text}")
    """
    以下エラー内容
    >>> Traceback (most recent call last):
    >>>   File "recv.py", line 16, in <module>
    >>>     recv_msg: bytes = socket_.recv(bufsize)
    >>> OSError: [Errno 107] Transport endpoint is not connected
    """
