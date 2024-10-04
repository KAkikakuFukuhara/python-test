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


    # データの送信
    text = "aaaa"
    print(f"Send:{text}")
    msg: bytes = text.encode()
    socket_.send(msg)
    """
    以下エラー内容
    >>> Traceback (most recent call last):
    >>>   File "send.py", line 18, in <module>
    >>>     socket_.send(msg)
    >>> BrokenPipeError: [Errno 32] Broken pipe
    """
