#Lesson 2:Private and public attributes/variables

class Show:
    def __init__(self,value):
        self.value1 = value
        self.value2 = value
        self.value3 = value

    def __str__(self):
        return f"vaue1: {self.value1} value2: {self.value2} value3: {self.value3}"

def main():
    s1 = Show(2)
    print(s1)

main()