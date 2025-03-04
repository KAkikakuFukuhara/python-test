""" finallyはexceptをキャッチしなくても実行されるのか実験
"""

try:
    raise Exception
finally:
    print("execute finally")
