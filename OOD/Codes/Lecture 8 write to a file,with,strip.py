#Lecture 8 - write to a file,with , strip()

def main():
    filename = 'lect8_out.txt'
    outfile = open(filename,'w')
    for num in range(5):
        print(num,file=outfile)
    outfile.close() #Must close file after writing

    try:
        with open(filename,'r') as datafile:
            for eachLine in datafile:
                print(eachLine.strip())
    except FileNotFoundError as error:
        print(error)

main()