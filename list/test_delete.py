import random
a = [ i if random.random() > 0.5 else None for i in range(100)]
print(a)

res = [b for b in a if b is not None]
print(res)

