""" finallyはreturnの後にも実行されるか？
"""

def func():
    try:
        return True
    finally:
        print("execute finally")

## 実行される
func()
