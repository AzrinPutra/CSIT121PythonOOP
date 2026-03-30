#Lecture 7 - try-except and loop

#Running while loop first and outside if the try-except block
def main():
    total = 0
    while True:
        try:
            num = int(input("Number?"))
            if num <0:
                break   #Break statement terminates the execution of the while loop immediately
            total += num
        except ValueError as error:
            print("Valueerror: ", error)
            print("Please enter a positive integer number")
    print(f'total = {total}')

main()