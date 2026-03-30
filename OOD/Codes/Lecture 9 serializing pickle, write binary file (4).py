#Lecture 9 serializing,deserializing,pickle,write and read binary file
import pickle
class Square:
    def __init__(self, side):
        self.__side =side
    def area(self):
        return self.__side ** 2

    def __str__(self):
        return f"{id(self)}, {self.__side}, {self.area()}"

def dumpLoadSquare():
    s1 = Square(5)
    s2 = Square(6)
    with open('lect9object.dat','wb') as bfile:
        pickle.dump(s1,bfile)
        pickle.dump(s2,bfile)

    with open('lect9object.dat','rb') as bfile:
        s11 = pickle.load(bfile)
        s12 = pickle.load(bfile)

    #compare
    print(s1 == s11)
    print(s2 ==s12)
    print("s1: ",s1)
    print("s11: ",s11)
    print("s2: ",s2)
    print("s12: ",s12)

def main():
    dumpLoadSquare()
    print("End of main")

main()