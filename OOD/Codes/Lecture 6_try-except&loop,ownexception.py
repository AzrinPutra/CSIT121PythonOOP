#Lecture 7 - try-except and loop and own eexception

class TemperatureException(Exception):  #ingerits Python Exception class
    pass    #pass because already inherited 

def convert(value):
    temperature = float(value)
    if temperature < 0 or temperature > 40:
        raise TemperatureException("Value out of range")
    return temperature

#Running while loop first and outside if the try-except block
def main():
    while True:
        try:
            value = input("Temperature: ")
            temperature = convert(value)
            if temperature == 0:
                break
            print(f"Temperature is {temperature}")
        except TemperatureException as error:
            print("Temperature error: ",error)
    print("End of program")

main()

#what if the user enters a character like b or z? How to raise this exception?