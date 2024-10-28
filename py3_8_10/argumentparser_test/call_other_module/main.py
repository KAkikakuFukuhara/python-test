from argparse import ArgumentParser

import called

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("a", type=str)
    parser.add_argument("b", type=str)
    cli_args = vars(parser.parse_args())

    called.main(**cli_args)