#Lecture 7 - *arg, **kwargs

def f1(*args):
    print(f"item1:{args}, item4: {args[3]}")

def f2(**kpara):
    print(f"p1:{kpara['p1']}")

def main():
    values = [20,30,40]
    f1(20,30,40,50) #passing multiplr values to *args which is a tuple
    f2(a1=301,p1=302,s3=303)    #passing key-value pairs to **kpara which is a dictionary

main()

#What if we want to pass a tuple to f1() and a dictionary to f2()