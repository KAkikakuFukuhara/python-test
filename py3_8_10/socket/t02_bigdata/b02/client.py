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
    ### 送信文字列の長さを1500にするとbufsize=1024だと全て文字列を受信できない
    text = ""
    text += "ab"*250
    text += "cd"*250
    text += "ef"*250
    print(f"Send:{text}")
    msg: bytes = text.encode()
    socket_.send(msg)
    ### 以下のようにすると b'' が送信される
    socket_.shutdown(socket.SHUT_WR)

    # データの受信
    bufsize = 1024
    recv_msg: bytes = socket_.recv(bufsize)
    recv_text: str = recv_msg.decode()
    print(f"Recv:{recv_text}")
    socket_.close()
