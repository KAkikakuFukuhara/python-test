""" 外部モジュールのインポートを関数化
"""
import importlib.machinery
import importlib.util
import sys
import importlib
from pathlib import Path
from types import ModuleType


def load_plugin(path: Path) -> ModuleType:
    loader = importlib.machinery.SourceFileLoader(str(mod_path), str(mod_path))
    spec = importlib.util.spec_from_file_location(str(mod_path), mod_path, loader=loader)
    assert spec is not None
    liba = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(liba)
    return liba


if __name__ == "__main__":
    mod_path = Path("/home/fukuhara/workspace/libknowledge/mypython/importlib/out_lib/liba.py")

    liba: ModuleType = load_plugin(mod_path)
    x = liba.Config()
    x.show()
