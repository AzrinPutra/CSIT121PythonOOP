#Lecture 5 - Inheritance, attribute
class Vehicle:
    def __init__(self, vehNum, capacity):
        self.__vehNum =vehNum
        self.__capacity = capacity

    def __str__(self):
        return f"vehNum= {self.__vehNum}, capacity= {self.__capacity}"

#Subclass
class Bus(Vehicle):
    def __init__(self, vehNum, capacity, regNo):
        super().__init__(vehNum,capacity)
        self.__regNo = regNo
    def __str__(self):
        return f"{super().__str__()}, regNo:{self.__regNo}"

def main():
    v = Vehicle('s84632c','1500cc')
    print(v)
    b = Bus('S3456Y','3200cc','R340395Z')
    print(b)
    all = [v,b,Bus('s1294A','1300cc','R294034X'),Vehicle('S3945V','1600cc')]
    for a in all:
        print(a)    #demostrate polymorphism where different objects are passed into print(), Python is able to execute the correct __str__()

if __name__ =='__main__':
    main()