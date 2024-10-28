import time


class MyGen:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield i


gen = MyGen(10)

epoch = int(1e7)

start_time = time.time()
for ei in range(epoch):
    for gj in gen:
        k = gj

elapd_time = time.time() - start_time

print(elapd_time)