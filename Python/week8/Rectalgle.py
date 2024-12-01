class Rectangle():
    """
    
    """
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        area = self.length * self.breadth
        return area
    def perimeter(self):
        perimeter = 2*self.length+self.breadth
        return perimeter
r = Rectangle(2,2)
print(r.area())
print(r.breadth)