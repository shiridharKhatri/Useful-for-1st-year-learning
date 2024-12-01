class Circle():
    def __init__(self, diameter, radius = 0):
        self.diameter = diameter
        self.radius = radius
    def area(self):
        pi = 3.14159265
        self.radius = self.diameter
        area = pi*self.diameter**2
        return area
c1 = Circle(4)
print(c1.area())