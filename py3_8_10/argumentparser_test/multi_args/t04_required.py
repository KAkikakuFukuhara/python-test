from argparse import ArgumentParser
import pprint


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-m", "--multi", type=int, nargs='+', required=True)
    kwargs = vars(parser.parse_args())
    pprint.pprint(kwargs)