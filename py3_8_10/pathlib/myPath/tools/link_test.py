import os
from argparse import ArgumentParser
from pathlib import Path
import glob
from typing import List
import shutil

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("src", type=str)
    parser.add_argument("dst", type=str)
    parser.add_argument("mode", choices=["absolute", "relative", "copy"])

    args = vars(parser.parse_args())

    return args


def main(args):
    src_dir = Path(args['src']).absolute().resolve()
    assert src_dir.exists()

    dst_dir = Path(args['dst']).absolute()
    assert dst_dir.parent.exists()
    if not dst_dir.exists():
        dst_dir.mkdir()

    src_files = [Path(p).absolute() for p in glob.glob(f"{src_dir}/*.txt")]

    mode = args['mode']
    if mode == "absolute":
        link_as_absolute(src_files, dst_dir)
    elif mode == "relative":
        link_as_relative(src_files, dst_dir)
    else: # mode == "copy"
        copy_files(src_files, dst_dir)


def link_as_absolute(src_files:List[Path], dst_dir:Path):
    for src_file in src_files:
        _src_file = src_file.resolve()
        _dst_dir = dst_dir.absolute()
        _dst_file = Path(f"{_dst_dir}/{_src_file.name}")
        print(f"{_src_file} -> {_dst_file}")
        os.symlink(_src_file, _dst_file)


def link_as_relative(src_files:List[Path], dst_dir:Path):
    for src_file in src_files:
        _src_file = src_file.absolute()
        _dst_dir = dst_dir.absolute()
        _dst_file = Path(f"{_dst_dir}/{_src_file.name}")
        _src_file = Path(os.path.relpath(_src_file, _dst_dir))
        os.symlink(_src_file, _dst_file)


def copy_files(src_files:List[Path], dst_dir:Path):
    for src_file in src_files:
        _src_file = src_file.absolute()
        _dst_dir = dst_dir.absolute()
        _dst_file = Path(f"{_dst_dir}/{_src_file.name}")
        shutil.copy(_src_file, _dst_file)


if __name__ == "__main__":
    args = parse_args()
    main(args)