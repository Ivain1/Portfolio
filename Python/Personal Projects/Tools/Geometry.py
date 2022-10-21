import math
from math import sqrt as root
Coord1 = [3,5]
Coord2 = [-5,-2]
pi = math.pi
def midpoint(C1,C2):
    Cx = (C1[0] + C2[0])/2
    Cy = (C1[1] + C2[1])/2
    return([Cx,Cy])

class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def perimeter(self):
        return(2*(self.b + self.l))
    def area(self):
        return(self.b*self.l)
    def diagonal(self):
        return(math.sqrt((self.b*self.b)*(self.l*self.l)))


class Circle:
    def __init__(self,radius):
        self.r = radius

    def perimeter(self):
        return(2*pi*self.r)

    def area(self):
        return(pi * (self.r * self.r))


rect1 = Rectangle(5,4)
print(rect1.perimeter())
print(midpoint(Coord1,Coord2))




