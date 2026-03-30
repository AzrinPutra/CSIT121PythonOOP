#Try-except
import logging

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

def getInventory():
    logfilename = 'lecture8_invlogger.txt'
    loggername = 'Inventory Logger'
    #Debug has the highest level
    logging.basicConfig(filename = logfilename, filemode = 'w', level = logging.DEBUG, force = True)
    invLogger = logging.getLogger(loggername)
    inventory={}
    #Assume get data from a file
    data = [['C100',10],[' ',10],['C101',-2],['C102',20]]
    for  codeQty in data:
        try:
            item = InventoryItem(codeQty[0],codeQty[1])
            inventory[codeQty[0]] = item

        except InventoryException as error:
            print(error)
            invLogger.error(f"{codeQty[0]} {codeQty[1]}, {error}")
    return inventory
def main():
    inventory = getInventory()
    for inv in inventory.values():
        print(inv)
main()