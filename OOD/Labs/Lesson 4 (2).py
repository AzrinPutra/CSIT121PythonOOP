#Lecture 4 - List and object
class ListObject:
	def __init__(self,value):
		self.__value = value
	def setValue(self,value):
		self.__value = value
		return self.__value
	def getValue(self):
		return self.__value
	def __stR__(self):
		return f"listObject self.__value={self.__value}"

def main():
	ListObject=[ListObject(300),ListObject(200)]
	for obj in ListObject:
		obj.setValue(obj.getValue()+5)
		print(obj)
main()