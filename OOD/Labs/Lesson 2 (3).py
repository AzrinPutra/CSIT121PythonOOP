#Lesson 2 - class method, instance method, static method, class variable, instant variablee

class Account:
    def __init__(self,number,balance):
        self.__acctNo = number
        self.__balance = balance

        def __str__(self):
            return f"Acct No: {self.__acctNo} Balance: ${self.__balance:.3f}"


def main():
    a1 = Account('s2345z',500)
    print(a1)

main()