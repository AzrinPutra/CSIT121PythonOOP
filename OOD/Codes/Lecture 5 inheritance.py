#Lecture 5 - Inheritance, circle, cylinder file
import math
class Circle:
	def __init__(self, radius):
		self.__radius = radius
	def getRadius(self):
		return self.__radius
	def __str__(self):
		return f"Access the circle class: radius {self.__radius}"

class Cylinder(Circle):
	def __init__(self,height, radius):
		self.__height = height
		super().__init__(radius)

	def __str__(self):
		return f"Access the cylinder class: height {self.__height} radius {super().getRadius()}"

def main():
	shapes = []
	filename = 'lect8_inputccy.txt'
	errorfilename = 'lect8_error.txt'
	try: 
		with open(filename,'r') as datafile, open(errorfilename,'w') as errorfile:
			for eachLine in datafile:
				try:
					values = eachLine.strip().split(',')
					if values[0] == 'c':
						shapes.append(Circle(float(values[1])))
					elif values[0] == 'cy':
						shapes.append(Cylinder(float(values[1]),float(values[2])))
				except ValueError as error:
					print(error)
					print(f"{error}, {values}",file = errorfile)

	except FileNotFoundError as error:
		print(error)
	for s in shapes:
		print(s)

main()
