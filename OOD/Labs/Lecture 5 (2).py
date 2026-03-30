import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        #print("Access circumference in Circle class")
        return 2 * math.pi * self.__radius

    def __str__(self):
        return f"Area ofcircle:{self.area():.2f} \
Circumference of circle:{self.circumference():.2f}"

class Cylinder(Circle):
    def __init__(self,height,radius):
        self.__height = height
        super().__init__(radius)

    def area(self): #same area() as Circle class
        topbottom = super().area() * 2  #specify access area() in superclass
        body = self.circumference() * self.__height
        return topbottom + body
    def volume(self):
        return self.__height * super().area()   #Specify access area() in Circle class

    def __str__(self):
        return f"Cylinder:Area={self.area()} Volume={self.volume()}"

def main():
    shapes = [Circle(1),Cylinder(10,2), Circle(2), Cylinder(5,3), Cylinder(6,4)]
    for s in shapes:
        print(s,s.area())
    print()
    for s in shapes:
        if isinstance(s,Cylinder):
            print("Cylinder is found")


main()