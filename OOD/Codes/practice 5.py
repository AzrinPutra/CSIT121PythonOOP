#Practice 5

def test0():
    data = ['hello','list','python']
    data.pop(1)
    print(data)
    data.remove('python')
    print(data)
    del data[1]
    print(data)

def test1():
    #Remove all values > 100
    #i is   0 1 2 3 4  6   7   8   9   10
    data = [1,2,3,4,5,100,105,106,150,109]
    for i in range(len(data)):   #Range(10)
        if data[i] > 100:
            print(i,data[i])
            data.pop(i)

def test2():
    data = [1,2,3,4,5,100,105,106,150,109]
    firstindex = len(data) - 1
    lastindex = -1
    for i in range(firstindex,lastindex,-1):
        if data[i] > 100:
            data.pop(i)
        print(data)

def test3():
    data = [1,2,3,4,5,100,105,106,150,109]
    to_be_deleted = []
    
    for value in data:
        if value > 100:
            to_be_deleted.append(value)

    print(data)
    print(to_be_deleted)

    for value in to_be_deleted:
        data.remove(value)
    print(data)

def test4():
    data = [1,2,3,4,5,100,105,106,150,109]
    to_be_deleted = [v for v in data if v >100]

    for value in to_be_deleted:
        data.remove(value)
    print(data)

def main():
    #test0()
    #test1()
    #test2()
    #test3()
    test4()

main()