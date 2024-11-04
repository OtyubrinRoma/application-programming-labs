import csv

class Iterator:
    def __init__(self, dir_annotation: str) -> None:
        self.dir_annotation = dir_annotation
        self.paths = self.load()
        self.limit = len(self.paths)
        self.counter = 0

    def __iter__(self) -> 'Iterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            next_self = self.paths[self.counter]
            self.counter += 1
            return next_self
        else:
            raise StopIteration

    def load(self) -> list:
        with open(self.dir_annotation, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            path_list = list(row[0] for row in reader)
            return path_list