if __package__ == 'lib':
    from utils.mydataclasses import A
else:
    from ..utils.mydataclasses import A

class B(A):
    def print(self):
        print("bbbb")