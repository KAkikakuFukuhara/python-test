# こちら側でcloseしたソケットへの send/recv

こちら側でcloseしたソケットへの send/recv コマンドの動作を以下に記述する。

## send

```console
Traceback (most recent call last):
  File "send.py", line 34, in <module>
    socket_.send(msg)
OSError: [Errno 9] Bad file descriptor    
```

## recv

```console
Traceback (most recent call last):
  File "recv.py", line 32, in <module>
    recv_msg: bytes = socket_.recv(bufsize)
OSError: [Errno 9] Bad file descriptor
```