#Lecture 9 serializing. pickle
import pickle
def dumpsLoads():
    grade = {'Andrew':86,'David':90}
    sGrade = pickle.dumps(grade)
    print(type(sGrade))
    print(len(sGrade))
    print(sGrade)
    rGrade = pickle.loads(sGrade)
    print(type(rGrade))
    print(rGrade)

def main():
    dumpsLoads()
    print("End of main")

main()