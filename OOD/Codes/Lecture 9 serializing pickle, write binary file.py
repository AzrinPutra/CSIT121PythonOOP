#Lecture 9 serializing. pickle
import pickle
def writeFile():
    grade = {'Andrew':86,'David':90}
    sGrade = pickle.dumps(grade)
    with open('lect9.dat','wb') as bfile:
        bfile.write(sGrade)
    print("End of write binary file")

def main():
    writeFile()
    print("End of main")

main()