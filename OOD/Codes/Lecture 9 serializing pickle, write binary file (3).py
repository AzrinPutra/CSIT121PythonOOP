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

def multipleLoad():
    with open('lect9multiple.dat',','):
        pickle.dump([1,2,3,4],bfile)
        pickle.dump({'Peter':'Smart'},bfile)
        pickle.dump("I am a string.",bfile)
    with open('lect9multiple.dat','rb') as bfile:
        obj = pickle.load(bfile)
        print(obj)
        obj = pickle.load(bfile)
        print(obj)
    data = []
    with open('lect9multiple.dat','rb') as bfile:
        try:
            while True:
                data.append(pickle.load(bfile))
        except EOFError as error:
            print(error)

        for item in data:
            print(type(item))
            print('Item in data list',item)



def main():
    multipleLoad()
    print("End of main")

main()