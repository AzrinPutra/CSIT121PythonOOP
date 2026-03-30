#Practice 3

def do_something(num):
    return num,num+100

def do_morething(num):
    return num,num+100,num+1000

def test2():
    r1,r2 = do_something(1)
    print(r1,r2)
    r4 = do_something(1)
    r5 = do_something(1)
    print(r4)
    print(r5)
    
def more_realistic():
    input_value = input("Enter 3 numbers: ")
    v = input_value.split()

    v1,v2,v3 = input_value.split()

 #    print(type(v))  #list
 #    print(type(v1),v1)  #str
 # #   print(type(v1),type(v2),type(v3))
 #    #Adding up numbers inside the list
    for each_v in v:
        total += int(each_v)
    #After loop
    print(total)
def about_list_comprehension():

    input_value = '10,20,30,40,10,5,60'
    list_str = input_value.split(',')
    list_num = []  #Empty list to hold number
    for each_str in list_str:
        list_num.append(int(each_str))
    print(list_str)
    print(list_num)
    #Using list comprehension to get the same result Compressing value into a string. Exact same asthe list.append but it is all inside 1 list with 
    # the int and for loop is placed inside
    list_num2 = [int(each_str) for each_str in list_str]
    print(list_num2)




def main():
    #test1()
    #test2()
    #more_realistic()
    about_list_comprehension()

# def test1():
    # add(1,2)
    # print(add(1,2))
    # total=add(1,2)
    # print(total)
    #Quick recap

def test2():
    None

main()