#Practice 1

def about_var():
    print('about_var')

def about_immutable_value():
    n1 = 10
    n2 = n1
    print(id(n1),n1) # 110
    print(id(n2),n2) # 10
    n1 = n1 + 100 
    print(id(n1),n1) # 110
    print(id(n2),n2) # 10

def about_str():
    s1 = '   abc   '
    s2 = s1.strip()
    s3 = s1.upper()
    print(id(s1),s1)
    print(id(s2),s2)
    print(id(s3),s3)
    #Changing a str variable??
    s1 = s1 + '4567890'
    print(id(s1),s1)

def main():
    #about_var()
    #about_immutable_value()
    about_str()
    print('End')

main()