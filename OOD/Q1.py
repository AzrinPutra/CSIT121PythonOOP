from datetime import date
class Course:
    def __init__(self,code,title,cost):
        self.__code = code
        self.__title = title
        self.__cost = float(cost)
    def get_code(self):
        return self.__code
    def get_title(self):
        return self.__title
    def get_cost(self):
        return self.__cost
    def __str__(self):
        return f"{self.__code}, {self.__title}, {self.__cost:2f}"
    def __eq__(self,other):
        if not isinstance(other,Course):
            return False
        return self.__code == other.__code
class Instructor:
    def __init__(self,email,name,rate):
        self.__email = email
        self.__name = name
        self.__rate = float(rate)
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_rate(self):
        return self.__rate
    def __str_(self):
        return f"{self.__name},{self.__email},{self.__rate:.2f}"
    def __eq__(self,other):
        if not isinstance(other,Instructor):
            return False
        return self.__email == other.__email
class CourseOffering:
    sch_id = 1

    def __init__(self,course,instructor, start_date,duration):
        self.__id = f'{course.get_code()}_{CourseOffering.sch_id}'
        CourseOffering.sch_id += 1
        self.__start_date = date
        self.__duration = int(duration)
        self.__course = course
        self.__instructor = instructor

    def get_start_date(self):
        return self.__start_date

    def get_email(self):
        return self.__instructor.get_email()

    def get_course_code(self):
        return self.__course.get_code()
    def get_course_fee(self):
        return self.__course.get_cost() + self.__start_date * self.__duration

    def __str__(self):
        return f'{self.__id},{self.__start_date},{self.__duration},{self.__course},{self.__instructor}'

    def __eq__(self,other):
        if not isinstance(other,self.__email):
            return False
        return self.__email == other.email


def get_course(filename):
    courses = []
    try:
        with open(filename,'r') as datafile:
            for line in datafile:
                line = line.strip()
                if line:
                    parts = line.split()

                    if len(parts) >= 3:
                        code =parts[0].strip()
                        title = parts[1].strip()
                        cost = float(parts[2].strip())
                        course = Course(code,title,cost)

                        if course not in courses:
                            courses.append(course)

    except FileNotFoundError as error:
        print(error)
    return courses


