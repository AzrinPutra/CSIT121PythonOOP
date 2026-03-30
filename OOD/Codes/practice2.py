#About function

def f(num):
    print('f',num)

 def main():
    #f1()
    f(100)

def f(num):
    print('f again', num + 1000)

def f1():
    print('f1')
    f2()

def f2():
    print('f2')
    f3()

def f3():
    print('f3')
  


main()
