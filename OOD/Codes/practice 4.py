#Practice 4

def test3():
    data = [10,20]
    #Create a new list containing values in data * 10
    data2 = []
    for i in range(len(data)):
        data2.append(data[i]*10)
    
    print(data2)

    #Solution 2
    data3 = []
    for each_value in data:
        data3.append(each_value * 10)
    print(data3)

    #Solution 3
    data4 = [v * 10 for v in data]
    print(data4)

def main():
    #test1()
    #test2()
    test3()
    print('End')

main()