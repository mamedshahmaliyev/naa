class GeometricObject:
    pi = 3.14159
    
    def calculateArea(self):
        pass
    
class Rectangle(GeometricObject):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculateArea(self):
        return self.width * self.height
    
class Circle(GeometricObject):
    def __init__(self, radius):
        self.radius = radius
    
    def calculateArea(self):
        return self.pi * self.radius * self.radius
    
class Triangle(GeometricObject):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculateArea(self):
        return 0.5 * self.base * self.height
    
