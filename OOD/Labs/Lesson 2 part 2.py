#Lesson 2: equality comparison
import math
class Point:
    def __init__(self,xCoord,yCoord):
        self.__x=xCoord
        self.__y=yCoord
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,xCoord):
        self.__x=xCoord
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,yCoord):
        self.__y=yCoord
    def distance(self): #assuming starting point is (0.0)
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def __str__(self):
        return f"xCoord:{self.__x} yCoord:{self.__y}"
def main():
    p1 = Point(1,2)
    p2 = Point(3,4)
    p3 = Point(5,6)
    print(p1)
    print(p2)
    print(p3)