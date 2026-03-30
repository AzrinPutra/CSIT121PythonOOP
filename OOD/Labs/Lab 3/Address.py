#For lab 3
class Address:
    def __init__(self, unit_block,street, city, state, postcode, country):
        self.__unit_block = unit_block
        self.__street = street
        self.__city = city
        self.__state = state
        self.__postcode = postcode
        self.__country = country

        def display(self):
            print(self)

        def __str__(self):
            return f"{self.__unit_block} {self.__street} {self.__city} {self.__state} {self.__postcode} {self.__country}\n"

def test_address():
    add = Address("A","Sim Ave", "W City", "UoW", "123", "Aust")
    add.display()

if __name__ == "__main__":
    test_address()
