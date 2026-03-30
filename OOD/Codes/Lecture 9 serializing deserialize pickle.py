#Lecture 9 serializing, deserializing, pickle
import pickle
def dumpsLoads():
    grade = {'Andrew':86,'David':90}
    sGrade = pickle.dumps(grade)
    rGrade = pickle.loads(sGrade)
    print(rGrade)
    print(id(grade))
    print(id(rGrade))
    print(grade==rGrade)

def main():
    dumpsLoads()
    print("End of main")

main()

#Why return True as the ids of grade and rGrade are different?
#because == operator calls __eq__() that compares the contents in the objects