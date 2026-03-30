
from A2 import Patient,Session,GeneralTherapy,SportsInjury,PostSurgeryRehab,PaediatricTherapy,ClinicBookingSystem
from datetime import date

def test_ClinicBookingSystem():
    try:
        system = ClinicBookingSystem()
        bd1 = date(1985,9,10)
        pid1 = system.add_patient("Alex Tan", bd1) #average patient
        bd2 = date(2020,5,22)
        pid2 = system.add_patient("Johnny", bd2)  # pediatric age
        bd3 = date(1959,1,15)
        pid3 = system.add_patient("Mr. Ong", bd3)    #senior (>=60)

        #check pid
        assert pid1<pid2 and pid2<pid3
        assert pid2-pid1==1 and pid3-pid2==1

        p1 = system.get_patient(pid1)
        assert p1.patient_id == pid1
        p2 = system.get_patient(pid2)
        assert p2.patient_id == pid2
        p3 = system.get_patient(pid3)
        assert p3.patient_id == pid3

        #General
        #General average and senior patient
        assert system.book_session("General",pid1,60,35,focus_area="Leg") == True
        assert system.book_session("General",pid3,60,35,focus_area="Leg") == True
        
        #Sports 
        #average non pro, average pro, senior non pro, senior pro
        assert system.book_session("Sports",pid1,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=False) == True
        assert system.book_session("Sports",pid1,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=True) == True
        assert system.book_session("Sports",pid3,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=False) == True
        assert system.book_session("Sports",pid3,60,35,sport_type="Tennis",injury_severity=1,pro_athlete=True) == True

        #PostSurgery
        #average, senior
        assert system.book_session("PostSurgery",pid1,60,35,surgery_type="Hip Replacement") == True
        assert system.book_session("PostSurgery",pid3,60,35,surgery_type="Hip Replacement") == True
  
        #Paediatric
        assert system.book_session("Paediatric",pid2,60,35,guardian_name="Mdm Lim") == True

        #get sessions for each patient
        assert len(system.get_sessions(pid1))==4
        assert len(system.get_sessions(pid2))==1
        assert len(system.get_sessions(pid3))==4

        print("Test ClinicBookingSystem class passed")
    except Exception:
        print("Test ClinicBookingSystem class failed")
 
def test_PaediatricTherapy():
    try:
        birthdate1 = date(2010, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = PaediatricTherapy(p1,60,35,"John")
        assert gt1.calculate_cost() == 63.0
        print("Test PediatricTherapy class passed")
    except Exception:
        print("Test PediatricTherapy class failed")

def test_PostSurgeryRehab():
    try:
        #non senior
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = PostSurgeryRehab(p1,60,35,"Hip Replacement")
        assert gt1.calculate_cost() == 80.5

        #senior
        birthdate2 = date(1950, 1, 1)
        p2 = Patient("John",birthdate2)
        gt2 = PostSurgeryRehab(p2,60,35,"Hip Replacement")
        assert gt2.calculate_cost() == 64.4 

        print("Test PostSurgeryRehab class passed")
    except Exception:
        print("Test PostSurgeryRehab class failed")

def test_SportsInjury():
    try:
        #non senior, non pro
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = SportsInjury(p1,60,35,"Tennis",1,False)
        assert gt1.calculate_cost() == 70.0

        #non senior, pro
        birthdate2 = date(1999, 1, 1)
        p2 = Patient("John",birthdate2)
        gt2 = SportsInjury(p2,60,35,"Tennis",1,True)
        assert gt2.calculate_cost() == 14.0

        # senior, non pro
        birthdate3 = date(1950, 1, 1)
        p3 = Patient("Bob",birthdate3)
        gt3 = SportsInjury(p3,60,35,"Tennis",1,False)
        assert gt3.calculate_cost() == 56.0

        #senior, Pro
        birthdate4 = date(1950, 1, 1)
        p4 = Patient("Jack",birthdate4)
        gt4 = SportsInjury(p4,60,35,"Tennis",1,True)
        assert gt4.calculate_cost()==11.2

        print("Test SportsInjury class passed")
    except Exception:
        print("Test SportsInjury class failed")

def test_GeneralTherapy():
    try:
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        gt1 = GeneralTherapy(p1,60,35,"Leg")
        assert gt1.calculate_cost() == 70.0

        #Senior
        birthdate2 = date(1950, 1, 1)
        p2 = Patient("John",birthdate2)
        gt2 = GeneralTherapy(p2,60,35,"Leg")
        assert gt2.calculate_cost() == 56.0
        print("Test GeneralTherapy class passed")
    except Exception:
        print("Test GeneralTherapy class failed")

def test_Patient():
    try:
        birthdate1 = date(1999, 1, 1)
        p1 = Patient("Peter",birthdate1)
        assert p1.patient_id == 1
        assert p1.__str__() == "Patient(id:1, name:Peter, age:26)"
        
        birthdate2 = date(2010, 4, 12)
        p2 = Patient("Peter",birthdate2)
        assert p2.patient_id == 2
        assert p2.__str__() == "Patient(id:2, name:Peter, age:15)"
        print("Test Patient class passed")
    except Exception:
        print("Test Patient class failed")

def main():
    test_Patient()
    test_GeneralTherapy()
    test_SportsInjury()
    test_PostSurgeryRehab()
    test_PaediatricTherapy()
    test_ClinicBookingSystem()

if __name__ == "__main__":
    main()