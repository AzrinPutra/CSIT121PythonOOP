import datetime


class School:
    def __init__(self,name):
        self._name = name
        self._employees = {}

        def add_emp(self, e):
            if e.empid in self._employees:
                return False
            self._employees[e.empid] = e
            return True

        def delete_emp(self, id):
            pass

        def find_emp(self, id):
            if id in self._employees:
                return self._employees[id]
            else:
                return None

        # def search_emp(self, subjects):
        #     emp = []
        #     for e in self._employees.values():
        #         print(f"Checking: {e}")
        #         if isinstance(e, AcademicEmp):      #Polymorphism
        #             if e.is_teaching(subjects):
        #                 emp.append(e)

        #     return emp
        def search_acad_emp_by_subject(self,subject):
            emps = [e for e in self.__employees.values() if (isinstance(e,AcademicEmp) and e.is_teaching(subject))]
            return emps

        def display(self):
            for emp_id in self.employees:
                print(self.__employees[emp_id])

def test_school():
    scit = School('school of IT')
    #Add ProfessionalEmp
    empid = 1
    name = "Bob"
    dob = datetime(1990, 5, 17)
    date_hired = datetime(2000,6,1)
