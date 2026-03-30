class Teacher:
    def __init__(self,staff_id,name):
        self.__staff_id = staff_id
        self.__name = name
        self.__subjects = []
    @property
    def staff_id(self):
        print("inside staff_id function ************")
        return self.__staff_id
    @property
    def name(self):      
        print("inside name() in Teacher class ")
        return self.__name
    @property
    def subjects(self):
        return self.__subjects
    def add_subject(self,subject):
        print("add subject in teacher class ----")
        self.subjects.append(subject)
    def remove_subject(self,subject):
        self.__subjects.remove(subject)
        def __str__(self):
            print("Enter print statement in Teacher class")
            subject_names = [subject.name for subject in self.__subjects]
            print("Next statement in Teacher class")
            subjects_str = ",".join(subject_names) if subject_names else "None"
            return f"Teacher ID: {self.__staff_id}\nTeacher Name:{self.__name}\nTeaching Subjects; {subjects_str}"

class Subject:
    def __init__(self,code,name):
        self.__code = code
        self.__name = name
        self.__teacher = None
        self.__students = []

    def get_code(self):
