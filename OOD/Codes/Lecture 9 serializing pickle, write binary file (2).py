#Lecture 9 serializing,deserializing,pickle,write and read binary file
import pickle
def writeFile():
    grade = {'Andrew':86,'David':90}
    sGrade = pickle.dumps(grade)
    with open('lect9.dat','wb') as bfile:
        bfile.write(sGrade)
    print("End of write binary file")

def readFile():
    with open('lect9.dat','rb') as bfile:
        obj = bfile.read()

    print(type(obj))
    print(obj)
    nGrade = pickle.loads(obj)
    print(type(nGrade))
    print(nGrade)

def main():
    readFile()
    print("End of main")

main()