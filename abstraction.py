from abc import ABC,abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*(self.radius**2)
    
def get_are_of_shape(shape):
    return shape.area()

rect=Rectangle(5,3)
circ=Circle(10)
        
# r=Rectangle(5,3)
# print(r.area())

print(get_are_of_shape(rect))
print(get_are_of_shape(circ))
