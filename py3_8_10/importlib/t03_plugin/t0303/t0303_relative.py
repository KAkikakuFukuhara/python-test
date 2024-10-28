""" 外部モジュールが既存のクラスの継承を利用している場合でメイン関数ではないところで呼び出されている
"""
import sys
from pathlib import Path

curr_path = Path(__file__)
root_path = curr_path.parent.parent
sys.path.insert(0, str(root_path))

from libs import config_loader

if __name__ == "__main__":
    mod_path = Path("/home/fukuhara/workspace/libknowledge/mypython/importlib/out_lib/configs/config2.py")

    x = config_loader.load_config(mod_path)
    x.show()
