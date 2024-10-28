# 通信のエラーが出た際のクライアント側の対処

 　クライアント側で通信のエラーが発生した際にクライアント側ではどのような対処をするべきかに関して検証を行う。

## 検証
 - 通信の仕様が異なる(Jsonの約束なのにJsonではない)
 - 同じ通信先に二回送受信
 - 再接続

### 通信の仕様が異なる(Jsonの約束なのにJsonではない)

 対象プログラム: client1.py  

 エラーは出ないがrecvで取得するデータがb''になる

### 同じ通信先に二回送受信

 対象プログラム: client2.py  
 
 二回目の送信で以下の例外が発生。
 ```console
 [Errno 32] Broken pipe
 ```
 recvはb''を取得する

### 再接続

 対象プログラム：client3_1.py  

 再接続を行う。以下の例外が発生。
 ```console
 Traceback (most recent call last):
   File "client3_1.py", line 71, in <module>
     cs.connect()
   File "client3_1.py", line 15, in connect
     self.socket.connect((self.ip_addr, self.port_num))
 OSError: [Errno 9] Bad file descriptor
 ```

 解決プログラム：client3_2.py  

 同一ソケットの再接続はダメなようなので毎回ソケットインスタンスを作り直すことで解決
