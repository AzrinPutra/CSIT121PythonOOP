#!/usr/bin/python3

import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__diameter = radius * 2

    # Method to compute area
    def area(self):
        return math.pi * (self.__radius**2)

    # Method to compute circumference
    def circumference(self):
        return 2 * math.pi * self.__diameter

    def __str__(self):
        return f"Circle with a radius of {self.__radius}"

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.__radius == other.__radius


def main():
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(5)

    print(c1)
    print(c1.area())
    print(c1.circumference())
    print(c2)
    print(c1 == c2)
    print(c1 == c3)


main()
