import importlib.machinery
import importlib.util
import sys
import importlib
from pathlib import Path
from types import ModuleType

from .config import Config


def load_plugin(path: Path) -> ModuleType:
    """
    Refalence:
        https://dev.classmethod.jp/articles/invalid-name-module-import/
    """
    loader = importlib.machinery.SourceFileLoader(str(path), str(path))
    spec = importlib.util.spec_from_file_location(str(path), path, loader=loader)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def load_config(path: Path) -> Config:
    print(Config)
    lib = load_plugin(path)
    print(lib.BaseConfig)
    return lib.Config()
