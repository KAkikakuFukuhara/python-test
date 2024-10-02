import socket
import json

if __name__ == '__main__':
    # 通信部分（ソケット）の準備
    family = socket.AF_INET # ipv4
    socket_ = socket.socket(family)

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

            # データの受信
            accum_msg = None
            while(True):
                bufsize = 1024
                recv_msg = child_socket.recv(bufsize)
                if recv_msg == b'':
                    break
                accum_msg = recv_msg if  accum_msg is None else accum_msg + recv_msg
            recv_text = accum_msg.decode() if accum_msg is not None else ''

            try:
                data_dict = json.loads(recv_text)
            except Exception as e:
                child_socket.close()
                continue

            print(f"Recv:{data_dict}")

            # データの送信
            text = "success"
            print(f"Send:{text}")
            msg = text.encode()
            child_socket.send(msg)
            child_socket.close()
    except KeyboardInterrupt:
        pass
