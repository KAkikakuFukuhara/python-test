from utils.classB import B

class C:
    def __init__(self):
        self.b = B()

    def print(self):
        self.b.print()