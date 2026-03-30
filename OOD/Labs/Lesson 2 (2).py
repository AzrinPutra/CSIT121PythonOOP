#Lesson 2:Private and public attributes/variables

class Show:
    def __init__(self,value):
        self.__radius = value
        self.__diameter = value

    def getRadius(self):
        return self.__radius

    def setRadius(self,value):
        self.__radius = value

    @property # @property declaration
    def diameter(self):
        return self.__diameter

    @diameter.setter #@diameter.setter declaration
    def diameter(self,value):
        self.__diameter = value

    def __str__(self):
        return f"Radius: {self.__radius} Diameter: {self.__diameter}"

def main():
    s1 = Show(25)
    print(s1.getRadius())
    s1.setRadius(50)
    print(s1.getRadius())

    #Using property
    s1.diameter=75  #set the attributes directly because of @diameter.setter
    print(s1.diameter) #Call the mthod without using () because of @property
    print(s1)
main()