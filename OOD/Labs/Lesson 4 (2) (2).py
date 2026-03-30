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
	def __eq__(self,other):	#eq = equal
		if other is None:
			return False
		if not isinstance(other,ListObject):
			return False
		return (self.__value==other.__value)


def main():
	listObject=[ListObject(100),ListObject(200)]
	data = ListObject(150)
	# for obj in ListObject:
	# 	obj.setValue(obj.getValue()+5)
	# 	print(obj)
	if data in listObject:
		print(True)
	else:
		print(False)
main()