#Lecture 8 - file I/O

def main():
    filename = 'lect8_textfile.txt'
    datafile = open(filename,'r')   #Whhat is return by open()
    entireFile = datafile.read()    #Read entire file, read()
    print(entireFile)   #output is one whole string
    datafile.seek(0)    #Move the file pointer to the beginning
    listStr = datafile.readlines()
    print(listStr)
    datafile.close()    #Must close the file


main()
