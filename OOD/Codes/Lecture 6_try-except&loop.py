#Lecture 7 - try-except and loop
def main():
    try:
        total = 0
        while True:
            num = int(input("Number?"))
            if num <0:
                break
            total += num
    except ValueError as error:
        print("Valueerror: ", error)
    except ZeroDivisionError as error:
        print("Dividebyzero error: ",error)
    else:
        print('else block executed - No error')
    finally:
        print('Executed all the time')
        print(f'total = {total}')

main()