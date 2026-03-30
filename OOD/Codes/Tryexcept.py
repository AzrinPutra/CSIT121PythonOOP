#Try-except

class InventoryException(Exception):
    pass
class InventoryItem:
    def __init__(self,prod,qty):
        if prod is None or len(prod) == 0:
            raise InventoryException("product code must not be empty")
        if qty<0:
            raise InventoryException("Quantity must be >=0")
        self.__prod = prod
        self.__qty = qty

    def __str__(self):
        return f"{self.__prod} with qty: {self.__qty}"

def main():
    item1 = InventoryItem('C1234',10)
    print(item1)
    try:
        item2 = InventoryItem('C1234',-10)

    except InventoryException as error:
        print(error)
    
    try: 
        item3 =InventoryItem(' ',10)

    except InventoryException as error:
        print(error)
    print("End of program")

main()