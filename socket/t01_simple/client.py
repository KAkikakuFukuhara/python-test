import socket


if __name__ == "__main__":
    # 通信部分（ソケット）の準備
    family = socket.AF_INET # ipv4
    socket_ = socket.socket(family)

    # クライアント側から接続依頼
    ip_addr: str = "127.0.0.1"
    port_num: int = 50001
    socket_.connect((ip_addr, port_num))

    # データの送信
    text = "aaaa"
    print(f"Send:{text}")
    msg: bytes = text.encode()
    socket_.send(msg)

    # データの受信
    bufsize = 1024
    recv_msg: bytes = socket_.recv(bufsize)
    recv_text: str = recv_msg.decode()
    print(f"Recv:{recv_text}")
    socket_.close()

