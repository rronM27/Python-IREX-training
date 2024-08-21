import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height*0.5

circle = Circle(5)
print(circle.area())
triangle = Triangle(5, 5)
print(triangle.area())
rectangle = Rectangle(5, 5)
print(rectangle.area())


