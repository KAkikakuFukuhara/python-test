import logging

import lib
from pkg import hoge2


logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    lib.test()

    logging.debug("debug")
    logging.info("info")
    logging.warning("warn")

    hoge2.test()
