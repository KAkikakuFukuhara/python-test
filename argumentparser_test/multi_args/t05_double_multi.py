from argparse import ArgumentParser
import pprint


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--multi1", type=int, nargs='+')
    parser.add_argument("--multi2", type=int, nargs='+')
    kwargs = vars(parser.parse_args())
    pprint.pprint(kwargs)