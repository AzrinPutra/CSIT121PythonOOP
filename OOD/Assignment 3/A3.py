from datetime import datetime, date

class Analytic:
    __errorfile = 'errors.txt'
    def __init__(self,filename):
        self.__movie = []
        try:
            with open(filename,'r') as datafile, open(Analytic.__errorfile,'w') as errorfile:

                for eachline in datafile:


        except FileNotFoundError as error:
            print(error)

    def get_genres():
        None

    def get_directors():
        pass    

    @property
    def count():
        pass
    def match():
        pass


