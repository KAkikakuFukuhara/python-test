""" 外部モジュールが既存のクラスの継承を利用している場合でメイン関数ではないところで呼び出されている
"""
from pathlib import Path

from libs import config_loader


if __name__ == "__main__":
    mod_path = Path("/home/fukuhara/workspace/libknowledge/mypython/importlib/out_lib/configs/config2.py")

    x = config_loader.load_config(mod_path)
    x.show()
