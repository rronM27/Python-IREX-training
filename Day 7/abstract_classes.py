from abc import ABC, abstractmethod #import Abatract Base Classes

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

katrori=Rectangle(5)
print(katrori.area())
print(katrori.perimeter())