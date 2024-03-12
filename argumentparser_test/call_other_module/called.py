from typing import Any, Dict
from argparse import ArgumentParser

def main(*args, **kwargs):
    print(kwargs)


def parse_args() -> Dict[str, Any]:
    parser = ArgumentParser()
    parser.add_argument("x", type=str)

    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":
    cli_args = parse_args()
    main(**cli_args)