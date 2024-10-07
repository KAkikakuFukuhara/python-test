""" 外部モジュールが既存のクラスの継承を利用している場合
"""
from libs import config_loader
from pathlib import Path


if __name__ == "__main__":
    mod_path = Path("/home/fukuhara/workspace/libknowledge/mypython/importlib/out_lib/configs/config2.py")

    config2 = config_loader.load_plugin(mod_path)
    x = config2.Config()
    x.show()
