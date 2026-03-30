from abc import abstractmethod
from datetime import datetime
from Address import Address

class Employee(ABC):
    __CPF_RATE = [[50,20], [60,12], [61,5]]
    def __init__(self, empid, name, dob, date_hired, address, m_number):
        self.__empid = empid
        self.__name = name
        self.__dob = dob
        self.__date_hired = date_hired
        self.__address = address
        self.__m_number = m_number
    @property
    def empid(self):
        return self.__empid
    @property
    def dob(self):
        return self.__dob
    @property
    def date_hired(self):
        return self.__date_hired
    @abstractmethod
    def get_annual_leave(self):
        pass
    def get_cpf_contribution(self):
        today = datetime.now()
        age = today.year - self.__dob.year
        #print('****',age)
        for age_contribution in Employee.__CPF_RATE:
            if age <=age_contribution[0]:
                cpf_contribution = age_contribution[1]
                break
        return cpf_contribution
    def __str__(self):
        s1 = f"{self.__empid} {self.__name}\n"
        s2 = f"DOB: {self.__dob}\n"
        s3 = f"Date hired: {self.__date_hired}\n"
        s4 = f"Mobile: {self.__m_number}\n"
        s5 = f"Address: {self.__address}\n"
        return s1 + s2 + s3 + s4 + s5

#Inheritance
class ProfessionalEmp(Employee):
    def __init__(self, empid, name, dob, date_hired, address, m_number, prof_position, working_days):
        super().__init__(empid, name, dob, date_hired, address, m_number)
        self.__prof_position = prof_position
        self.__working_days = working_days

    def get_annual_leave(self):
        years_hired = datetime.now().year - self.date_hired.year
        #print("Years hired", years_hired)
        if years_hired < 2:
            return 15
        elif years_hired < 4:
            return 18
        else:
            return 21

#Inheritance
class AcademicEmp(Employee):
    def __init__(self, empid, name, dob, date_hired, address, m_number, acad_pos):
        super().__init__(self, empid, name, dob, date_hired, address, m_number)
        self.__acad_pos = acad_pos
        self.__teaching_subject = []
        self.__research_area = []
    
    def add_subject(self, teaching_subject):
        if teaching_subject not in self.__teaching_subject:
            self.__teaching_subject.append(teaching_subject)
    def add_research_area(self, research_area):
        if research_area not in self.__research_area:
            self.__research_area.append(research_area)

    def get_annual_leave(self):
        return 14

    def is_teaching(self,subject):
        for s in self.__teaching_subject:
            if s == subject:
                return True
        #Not teaching
        return False

    def __str__(self):
        mesg = ""
        if len(self.__teaching_subject) == 0:
            mesg += "No teaching subject\n"
        else:
            mesg += "Teaching subjects:"
            mesg += ", ".join(self.__teaching_subject) + "\n"

        if len(self.__research_area) == 0:
            mesg += "No research area\n"
        else: 
            mesg +="Research areas:"
            mesg +=", ".join(self.__research_area) + "\n"

        return f"{super().__str__()} {mesg}"

