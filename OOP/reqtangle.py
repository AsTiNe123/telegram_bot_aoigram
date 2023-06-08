
from math import pi
from ABC import Shape

class Reqtangle(Shape):
    def __init__(self, hight, width ) -> None:
        self.hight = hight
        self.wight = width

    def perim(self):
        return 2*self.hight + 2*self.wight
    
    def sqwer(self):
        return self.hight * self.wight
    

class Sqhare(Reqtangle):
    def __init__(self, length):
        super().__init__(length, length)

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def sqwer(self):
        return pi * self.radius**2
    
    def perim(self):
        return 2 * pi * self.radius

        



reqtangle = Reqtangle(2, 4)

sqhare = Sqhare(4)

circle = Circle(5)

print(reqtangle.perim(), sqhare.perim(), circle.perim())
print(reqtangle.sqwer(), sqhare.sqwer(), circle.sqwer())