def loadtext():
    filename = 'resultv2.txt'
    with open(filename,'r') as datafile:
        for eachLine in datafile:
            value = eachLine.strip().split(',')

            if value[0][0] in ['W']:
                print(eachLine)
                print(value[1],'   ',value[4],'\n')

def main():
    loadtext()

main()