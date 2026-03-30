#Lecture 7 - exception handling
def main():
    try:
        num = int(input("Number?"))
        print(f"10/{num} is {10/num}")
        print("End of try block")

    except ValueError as error:
        print("Valueerror: ", error)
    except ZeroDivisionError as error:
        print("Dividebyzero error: ",error)
    else:
        print('else block executed - No error')
    finally:
        print('Executed all the time')

main()