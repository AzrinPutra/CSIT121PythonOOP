import math
class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

class Circle:
    def __init__(self,center_x,center_y,radius):
        self.__center = Point(center_x,center_y)
        self.__radius = radius
    def area(self):
        return math.pi * self.__radius ** 2
    def circumference(self):
        return 2 * math.pi * self.__radius

    #assume the angle is in degree
    def point_coordinates(self,angle):
        phi = math.radians(angle)
        x = self.__radius * math.cos(phi) + self.__center.getX()
        y = self.__radius * math.sin(phi) + self.__center.getY()
        return Point(x,y)
     
if __name__ == '__main__':
    #Create a circle based on user's inputs
    center_x = float(input("Enter the x-coordinate of the circle's center: "))
    center_y = float(input("Enter the y-coordinate of the circle's center: "))
    radius = float(input("Enter the radius ofthe circle: "))
    circle = Circle(center_x,center_y,radius)

    #Calculate and print the area and circumference of the circle
    print("Area: ",circle.area())
    print("Circumference: ",circle.circumference())
    #Calculate and print the coordinate of the point on the circle based on the angle
    angle = float(input("Enter the angle(in degree): "))
    point = circle.point_coordinates(angle)
    print("Point coordinates: ",point.getX(),point.getY())