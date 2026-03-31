# OOP, class, object, __init__, __str__, __eq__
#!/usr/bin/python3


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    # Method to compute area
    def area(self):
        return self.__length * self.__width

    # Return a str that represent a Rectangle object
    def __str__(self):
        return f"Rectangle of {self.__length} x {self.__width}"


def main():
    r1 = Rectangle(20, 10)
    r2 = Rectangle(10, 1)
    print(r1)
    print(r2)
    a1 = r1.area()
    a2 = r2.area()
    print(f"a1 is {a1}")
    print(f"a2 is {a2}")

    # list of Rectangle objects
    rect = [Rectangle(20, 10), Rectangle(10, 1)]
    for r in rect:
        print(r)
        print(r.area())

    # Converting from nested list of numbers to list of Rectangle
    data = [[20, 2], [10, 5], [5, 1]]
    rectList1 = []
    for i in data:
        rectList1.append(Rectangle(i[0], i[1]))

    print("List of Rectangle objects")
    for r in rectList1:
        print(r)


main()
