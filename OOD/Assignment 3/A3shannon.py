from datetime import datetime, date

class Analytic:
    __errorFile = 'errors.txt'
    def __init__(self, file):
        self.__movies = []
        try:
            with open(file, 'r') as datafile, open(Analytic.__errorFile, 'w') as errorfile:
                skipLine1 = datafile.readline() # Skip header
                
                line_no = 2
                for eachLine in datafile:
                    errors = []
                    values = eachLine.strip().split(',')                 
                    
                    Title, Genre, YOR_raw, Director, Studio, GlobalSales_raw, CriticScore_raw, Rating = values
                    
                    # check for empty
                    if Title == '':
                        errors.append('Column 1 is Empty')
                    if Genre == '':
                        errors.append('Column 2 is Empty')
                    if YOR_raw == '':
                        errors.append('Column 3 is Empty')
                    if Director == '':
                        errors.append('Column 4 is Empty')
                    if Studio == '':
                        errors.append('Column 5 is Empty')
                    if GlobalSales_raw == '':
                        errors.append('Column 6 is Empty')
                    if CriticScore_raw == '':
                        errors.append('Column 7 is Empty')
                    if Rating == '':
                        errors.append('Column 8 is Empty')
                    
                    # --- numeric checks ---
                    YOR = None
                    GlobalSales = None
                    CriticScore = None
                    
                    # Year_Released
                    if YOR_raw != '':
                        try:
                            YOR = int(YOR_raw)
                            if YOR < 1990 or YOR > date.today().year:
                                errors.append("Year_Released out of range")
                        except ValueError:
                            errors.append("Invalid Year_Released")
                            
                    # Global_Sales
                    if GlobalSales_raw != '':
                        try:
                            GlobalSales = float(GlobalSales_raw)
                        except ValueError:
                            errors.append("Global_Sales is not numeric")                        
                    
                    # Critic_Score
                    if CriticScore_raw != '':
                        try:
                            CriticScore = int(CriticScore_raw)
                            if CriticScore < 0:
                                errors.append("Critic_Score is negative")
                            elif CriticScore > 100:
                                errors.append("Critic_Score greater than 100")
                        except ValueError:
                            errors.append("Critic_Score is not numeric")
                    
                    # --- write errors ---
                    if errors:
                        error_line = f'Line {line_no}: '
                        for i in  range(len(errors)):
                            error_line += errors[i]
                            if i < len(errors) -1:
                                error_line += ', '
                        error_line += "\n"
                        print(error_line.strip(), file=errorfile)
                        
                    else:
                        # Add valid data to list
                        IndvMovie = {
                            'title': Title,
                            'genre': Genre,
                            'year_of_release': YOR,
                            'director': Director,
                            'studio': Studio,
                            'global_sales': GlobalSales,
                            'critic_score': CriticScore,
                            'rating': Rating}
                        
                        self.__movies.append(IndvMovie)
                    line_no +=1
                    
        except FileNotFoundError as e:
            print(e)

    def get_genres(self):
        genreList = []
        for IndvMovie in self.__movies:
            genre = IndvMovie['genre']
            if genre not in genreList:
                    genreList.append(genre)
        return genreList
    
    def get_directors(self):
        directorList = []
        for IndvMovie in self.__movies:
            director = IndvMovie['director']
            if director not in directorList:
                    directorList.append(director)
        return directorList
    
    @property
    def count(self):
        if len(self.__movies) == 0:
            return False
        return len(self.__movies)
        
    
    def match(self, title=[], genre=[], year_of_release=[], director=[], studio=[], global_sales=[], critic_score=[], rating=[]):
        matchList = []
       
        for IndvMovie in self.__movies:            
            match = True  # Assume it matches until proven otherwise

            # ---- title ----
            if title and IndvMovie['title'] not in title:
                match = False

            # ---- genre ----
            if genre and IndvMovie['genre'] not in genre:
                match = False

            # ---- year_of_release ----
            if year_of_release:
                low, high = year_of_release
                if low >= 1990 and high <= date.today().year:
                    if not (low <= IndvMovie['year_of_release'] <= high):
                        match = False

            # ---- director ----
            if director and IndvMovie['director'] not in director:
                match = False

            # ---- studio ----
            if studio and IndvMovie['studio'] not in studio:
                match = False

            # ---- global_sales ----
            if global_sales:
                low, high = global_sales
                if low >= 0:
                    if not (low <= IndvMovie['global_sales'] <= high):
                        match = False

            # ---- critic_score ----
            if critic_score:
                low, high = critic_score
                if low >= 0 and high <= 100:
                    if not (low <= IndvMovie['critic_score'] <= high):
                        match = False

            # ---- rating ----
            if rating and IndvMovie['rating'] not in rating:
                match = False

            # ---- final add ----
            if match:
                matchList.append(IndvMovie)

        return matchList