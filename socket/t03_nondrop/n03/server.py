import socket
import json


def communicate(socket_: socket.socket):
    ### データの受信
    accum_msg = None
    while(True):
        bufsize = 1024
        recv_msg = child_socket.recv(bufsize)
        if recv_msg == b'':
            break
        accum_msg = recv_msg if  accum_msg is None else accum_msg + recv_msg
    recv_text = accum_msg.decode() if accum_msg is not None else ''

    ### データの変換
    data_dict = json.loads(recv_text)
    print(f"Recv:{data_dict}")

    ### データの送信
    text = "success"
    print(f"Send:{text}")
    msg = text.encode()
    child_socket.send(msg)


if __name__ == '__main__':
    # 通信部分（ソケット）の準備
    family = socket.AF_INET # ipv4
    socket_ = socket.socket(family)
    socket_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # サーバー側の接続の受信待機
    ip_addr: str = "127.0.0.1"
    port_num: int = 50001
    socket_.bind((ip_addr, port_num))

    ### エラーが起きたら再接続待ちをするように変更する
    print("EXIT = ctrl+c")
    try:
        while(True):
            socket_.listen(1)
            child_socket, client_address = socket_.accept()
            print(f"acceept (IP, Port)={client_address}")

            try:
                communicate(socket_)
            except Exception as e:
                print(type(e), e)
            finally:
                child_socket.close()
                print("close socket")
    except KeyboardInterrupt:
        pass
