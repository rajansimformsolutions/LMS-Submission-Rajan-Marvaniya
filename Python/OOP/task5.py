from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2
    
R = rectangle(10,5)
C = circle(7)

print("rectangle area:", R.calculate_area())
print("circle area:", C.calculate_area())