if __package__ == 'lib':
    from utils.mydataclasses import Dataset
else:
    from ..utils.mydataclasses import Dataset

class DataLoader:
    def load_data(self, path:str):
        with open(path, "r") as f:
            src = f.read()

        dataset = Dataset(src)
        return dataset