class Rectangle:
	def __init__(self,length,width):
		print(f" inside __init__ length = {length}, width = {width}")
		self.__length = length
		self.__width = width
	def __str__(self):
		return f"Rectangle: {self.__length} {self.__width}"

def main():
	rect1 = Rectangle(20,15)
	rect2 = Rectangle(10,5)
	print(rect1)
	print(rect2)

	print(Rectangle(2,3))
main()

# __init__() and __str__() are special methods	