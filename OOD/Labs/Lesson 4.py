#Lecture 4 - List and loop
def listloop2():	#Access a list item and add 300 and put new value in a variable called data
	list2=[1,2]
	for data in list2:
		data += 300	#Put new value in a variable called data
		print("Data =", data)
	print("list2=", list2)	#Value in list2 are unchanged


#How to put a new value back into the list item?
def listloop3():	#Access a list item and add 300 and put new value backinto the list item
	list3 = [1,2]
	for i in range(len(list3)):
		list3[i] += 300	#Put new value back into the list item
		print(f"list3[{i}]={list3[i]}")
	print("list3=",list3)	#Value in list3 are updated
	0
def main():
	listloop2()

	listloop3()

main()
