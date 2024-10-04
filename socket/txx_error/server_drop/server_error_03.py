import socket
import time

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

    ### ** error Pre-Client-send **
    try:
        raise Exception
    except Exception as e:
        print(e)
        child_socket.shutdown(socket.SHUT_RDWR)
        child_socket.close()
        while(True):
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                exit(1)

    # データの受信
    bufsize = 1024
    recv_msg = child_socket.recv(bufsize)
    recv_text = recv_msg.decode()
    print(f"Recv:{recv_text}")


    # データの送信
    text = "success"
    print(f"Send:{text}")
    msg = text.encode()
    child_socket.send(msg)
    child_socket.close()
