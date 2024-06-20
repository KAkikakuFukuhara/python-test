from argparse import ArgumentParser
import pprint


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("multi", type=int, nargs='*')
    kwargs = vars(parser.parse_args())
    pprint.pprint(kwargs)