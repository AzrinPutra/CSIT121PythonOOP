#Lecture 8 - file I/O

def main():
    filename = 'lect8_textfile.txt'
    datafile = open(filename,'r')   #Whhat is return by open()
    for oneLine in datafile:
        print(oneLine.strip())  #Strip used to clear empty spaces
    datafile.close()    #Must close the file


main()
