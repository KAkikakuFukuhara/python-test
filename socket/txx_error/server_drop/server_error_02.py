import socket


if __name__ == '__main__':
    # 通信部分（ソケット）の準備
    family = socket.AF_INET # ipv4
    socket_ = socket.socket(family)
    socket_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # サーバー側の接続の受信待機
    ip_addr: str = "127.0.0.1"
    port_num: int = 50001
    socket_.bind((ip_addr, port_num))
    socket_.listen(1)
    child_socket, client_address = socket_.accept()

    # データの受信
    bufsize = 1024
    recv_msg = child_socket.recv(bufsize)
    recv_text = recv_msg.decode()
    print(f"Recv:{recv_text}")

    ### ** error after-client-send **
    raise Exception

    # データの送信
    text = "success"
    print(f"Send:{text}")
    msg = text.encode()
    child_socket.send(msg)
    child_socket.close()
