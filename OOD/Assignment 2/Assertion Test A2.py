from A2 import Patient,Session,GeneralTherapy,SportsInjury,PostSurgeryRehab,PaediatricTherapy,ClinicBookingSystem
from datetime import date

case_num = 1

def show_result(passed):
    global case_num
    if passed:
        print(f"Case {case_num} pass")
    else:
        print(f"Case {case_num} fail")
    case_num += 1

def test_ClinicBookingSystem():
    global case_num
    try:
        system = ClinicBookingSystem()
        bd1 = date(1985,9,10)
        pid1 = system.add_patient("Alex Tan", bd1)
        bd2 = date(2020,5,22)
        pid2 = system.add_patient("Johnny", bd2)
        bd3 = date(1959,1,15)
        pid3 = system.add_patient("Mr. Ong", bd3)

        show_result(pid1 < pid2 and pid2 < pid3)
        show_result(pid2 - pid1 == 1 and pid3 - pid2 == 1)

        p1 = system.get_patient(pid1)
        show_result(p1.patient_id == pid1)
        p2 = system.get_patient(pid2)
        show_result(p2.patient_id == pid2)
        p3 = system.get_patient(pid3)
        show_result(p3.patient_id == pid3)

        show_result(system.book_session("General",pid1,60,35,focus_area="Leg") == True)
        show_result(system.book_session("General",pid3,60,35,focus_area="Leg") == True)
        show_result(system.book_session("Sports",pid1,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=False) == True)
        show_result(system.book_session("Sports",pid1,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=True) == True)
        show_result(system.book_session("Sports",pid3,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=False) == True)
        show_result(system.book_session("Sports",pid3,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=True) == True)
        show_result(system.book_session("PostSurgery",pid1,60,35,surgery_type="Hip Replacement") == True)
        show_result(system.book_session("PostSurgery",pid3,60,35,surgery_type="Hip Replacement") == True)
        show_result(system.book_session("Paediatric",pid2,60,35,guardian_name="Mdm Lim") == True)

        show_result(len(system.get_sessions(pid1)) == 4)
        show_result(len(system.get_sessions(pid2)) == 1)
        show_result(len(system.get_sessions(pid3)) == 4)
    except Exception:
        show_result(False)

def test_PaediatricTherapy():
    global case_num
    try:
        birthdate1 = date(2010, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = PaediatricTherapy(p1,60,35,"John")
        show_result(gt1.calculate_cost() == 63.0)
    except Exception:
        show_result(False)

def test_PostSurgeryRehab():
    global case_num
    try:
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = PostSurgeryRehab(p1,60,35,"Hip Replacement")
        show_result(gt1.calculate_cost() == 80.5)

        birthdate2 = date(1950, 1, 1)
        p2 = Patient("John",birthdate2)
        gt2 = PostSurgeryRehab(p2,60,35,"Hip Replacement")
        show_result(gt2.calculate_cost() == 64.4)
    except Exception:
        show_result(False)

def test_SportsInjury():
    global case_num
    try:
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = SportsInjury(p1,60,35,"Tennis",1,False)
        show_result(gt1.calculate_cost() == 70.0)

        birthdate2 = date(1999, 1, 1)
        p2 = Patient("John",birthdate2)
        gt2 = SportsInjury(p2,60,35,"Tennis",1,True)
        show_result(gt2.calculate_cost() == 14.0)

        birthdate3 = date(1950, 1, 1)
        p3 = Patient("Bob",birthdate3)
        gt3 = SportsInjury(p3,60,35,"Tennis",1,False)
        show_result(gt3.calculate_cost() == 56.0)

        birthdate4 = date(1950, 1, 1)
        p4 = Patient("Jack",birthdate4)
        gt4 = SportsInjury(p4,60,35,"Tennis",1,True)
        show_result(gt4.calculate_cost() == 11.2)
    except Exception:
        show_result(False)

def test_GeneralTherapy():
    global case_num
    try:
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = GeneralTherapy(p1,60,35,"Leg")
        show_result(gt1.calculate_cost() == 70.0)

        birthdate2 = date(1950, 1, 1)
        p2 = Patient("John",birthdate2)
        gt2 = GeneralTherapy(p2,60,35,"Leg")
        show_result(gt2.calculate_cost() == 56.0)
    except Exception:
        show_result(False)

def test_Patient():
    global case_num
    try:
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        show_result(p1.patient_id == 1)
        show_result(p1.__str__() == "Patient(id:1, name:Peter, age:26)")

        birthdate2 = date(2010, 4, 12)
        p2 = Patient("Peter",birthdate2)
        show_result(p2.patient_id == 2)
        show_result(p2.__str__() == "Patient(id:2, name:Peter, age:15)")
    except Exception:
        show_result(False)

def main():
    test_Patient()
    test_GeneralTherapy()
    test_SportsInjury()
    test_PostSurgeryRehab()
    test_PaediatricTherapy()
    test_ClinicBookingSystem()

if __name__ == "__main__":
    main()
