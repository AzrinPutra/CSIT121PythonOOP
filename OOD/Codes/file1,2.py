from file1 import f1,f2 
from file2 import f1 as ff1,f2 as ff2 #Save f1 & f2 as a new function name as to not get overwritten and cause bug with conflicting function name

def main():
    f1()    #Inside file1 f1
    f2()    #Inside file1 f2
    ff1()   #Inside file2 f1
    ff2()   #Inside file 2 f2

main()
