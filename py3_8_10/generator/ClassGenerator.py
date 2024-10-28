import time

class MyGenerator:
    def __init__(self):
        self.data = [i for i in range(10)]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for i in self.data:
            yield i
        return

gen = MyGenerator()

#for i in tqdm.tqdm(range(10)):
#    for x in tqdm.tqdm(gen, leave=False):
#        time.sleep(0.1)

for i in range(2):
    for j, x in enumerate(gen):
        print(x)


