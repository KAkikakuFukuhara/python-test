import time

def mygen(n):
    for i in range(n):
        yield i

epoch = int(1e7)

start_time = time.time()
for ei in range(epoch):
    for gj in mygen(10):
        k = gj

elapd_time = time.time() - start_time

print(elapd_time)