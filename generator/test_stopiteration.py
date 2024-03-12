import random

class MyIterator:
    def __init__(self):
        self.data = [ i for i in range(10)]
        self.current = 0

    def __next__(self):
        if self.current >= len(self.data):
            self.current = 0
            raise StopIteration

        res = self.data[self.current] 
        self.current += 1
        return res

    def __iter__(self):
        random.shuffle(self.data)
        return self


myite = MyIterator()
for i in range(2):
    for j in myite:
        print(f"{i}:{j}")

