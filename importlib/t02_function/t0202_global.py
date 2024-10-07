""" 外部モジュールのインポートを返り値に依存しないようにする
"""
import importlib.machinery
import importlib.util
import sys
import importlib
from pathlib import Path
from types import ModuleType


liba: ModuleType


def load_plugin(path: Path):
    loader = importlib.machinery.SourceFileLoader(str(mod_path), str(mod_path))
    spec = importlib.util.spec_from_file_location(str(mod_path), mod_path, loader=loader)
    assert spec is not None
    global liba
    liba = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(liba)


if __name__ == "__main__":
    mod_path = Path("/home/fukuhara/workspace/libknowledge/mypython/importlib/out_lib/liba.py")

    load_plugin(mod_path)
    x = liba.Config()
    x.show()
