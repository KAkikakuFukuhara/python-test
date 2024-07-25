""" subclassを使ったプロセス間通信
"""
import sys
import time
import signal
import multiprocessing as mp


def signal_handler(signum, frame):
    sys.exit(1)


class SubProcess(mp.Process):
    def run(self):
        print(self.name)
        return


if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = SubProcess()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
