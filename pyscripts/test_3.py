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

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(
            other, Rectangle
        ):  # takes two positionals -> reference and object
            return False
        return self.__length == other.__length and self.__width == other.__width


def main():
    r1 = Rectangle(2, 1)
    r2 = Rectangle(2, 1)
    r3 = Rectangle(3, 1)

    print(r1 == r2)
    print(r2 == r1)
    print(r1 == r3)
    print(r1.__eq__(r2))  # r1 == r2
    print(r2.__eq__(r1))  # r2 == r1
    print(r1.__eq__(r3))  # r1 == r3

    # Error handling
    r4 = None
    print(r1 == r4)
    r5 = "Python"
    print(r1 == r5)


main()
