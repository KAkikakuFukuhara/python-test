from argparse import ArgumentParser
import pprint

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("--a", action='store_true')
    args = vars(parser.parse_args())

    pprint.pprint(args)

if __name__ == "__main__":
    parse_args()