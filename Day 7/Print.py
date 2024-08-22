from abc import ABC, abstractmethod

class Pritable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Pritable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def print_info(self):
        print(f"Book: {self.title} by {self.author}")

libri=Book("the great gatby", "F Scott FitzGerald", '1700')
libri.print_info()