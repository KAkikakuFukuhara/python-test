# 接続が失敗したソケットへの send/recv

接続が失敗したソケットへの send/recv コマンドの動作を以下に記述する。

## send

```console
Traceback (most recent call last):
  File "send.py", line 18, in <module>
    socket_.send(msg)
BrokenPipeError: [Errno 32] Broken pipe
```

## recv

```console
Traceback (most recent call last):
  File "recv.py", line 16, in <module>
    recv_msg: bytes = socket_.recv(bufsize)
OSError: [Errno 107] Transport endpoint is not connected
```