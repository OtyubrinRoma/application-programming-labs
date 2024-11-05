import csv

class Iterator:
    def __init__(self, dir_annotation: str) -> None:
        """
        Read each line of the annotation file and output the corresponding field
        :param dir_annotation: path to the annotation file
        """
        self.dir_annotation = dir_annotation
        self.paths = self.__load()
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

    def __load(self) -> list:
        with open(self.dir_annotation, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            path_list = list(row[0] for row in reader)
            return path_list