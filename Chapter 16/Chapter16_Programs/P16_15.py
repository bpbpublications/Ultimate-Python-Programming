from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def draw(self):
        print('Drawing a rectangle')

class Triangle(Shape):
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        sp = (self.s1 + self.s2 + self.s3) / 2
        return (sp * (sp - self.s1) * (sp - self.s2) * (sp - self.s3)) ** 0.5

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def draw(self):
        print('Drawing a triangle')


r1 = Rectangle(13, 25)
t1 = Triangle(14, 17, 12)

r1.draw()
t1.draw()
print(r1.area())
print(t1.area())