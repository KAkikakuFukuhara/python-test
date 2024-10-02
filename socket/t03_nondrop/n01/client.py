import socket
import json


if __name__ == "__main__":
    # 通信部分（ソケット）の準備
    family = socket.AF_INET # ipv4
    socket_ = socket.socket(family)

    # クライアント側から接続依頼
    ip_addr: str = "127.0.0.1"
    port_num: int = 50001
    socket_.connect((ip_addr, port_num))

    # データの送信
    ### 複雑なデータを送るにはjsonを使うてもある
    data_dict = {}
    data_dict['command'] = 'process'
    data_dict['text'] = "ab"*250 + "cd"*250 + "ef"*250
    print(f"Send:{data_dict}")
    ### 一回文字列にしてからbytes型にエンコードする
    text = json.dumps(data_dict)
    msg: bytes = text.encode()
    raise Exception
    socket_.send(msg)
    socket_.shutdown(socket.SHUT_WR)

    # データの受信
    bufsize = 1024
    recv_msg: bytes = socket_.recv(bufsize)
    recv_text: str = recv_msg.decode()
    print(f"Recv:{recv_text}")
    socket_.close()
