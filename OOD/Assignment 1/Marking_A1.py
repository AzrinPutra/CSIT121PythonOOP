#rename your python file as A1.py and grade your Assignment
from A1 import Trainee,Trainer,ExerciseSession,PersonalTrainingManagementSystem
from datetime import datetime, date

score = 0

def get_non_private_instance_variables(obj):
    """
    Returns a list of non-private instance variables of the given object.
    """
    return [key for key in vars(obj) if not key.startswith('_')]

def testTrainee():
    try:
        birthdate = date(1999, 12, 1)
        t = Trainee(1,"John",birthdate,"abc@gmail.com")
        age = t.get_age()
        assert age==25
        assert t.__str__() == "Trainee(id:1, name:John, birthdate:1999-12-1, email=:abc@gmail.com, age:25)"
        print("Test Trainee passed")
        return True
    except Exception as error:
        print("Test Trainee failed")
        return False    
    
def testTrainer():
    try:
        t = Trainer(1,"Peter")
        assert t.__str__() == "Trainer(id:1, name:Peter)"
        print("Test Trainer passed") 
        return True
    except Exception as error:
        print("Test Trainer failed")
        return False  
    
def testExerciseSession():
    try:
        session_date = date(2025, 9, 1)
        s = ExerciseSession(1,1,1,30,1,session_date)
        assert s.__str__() == "ExerciseSession(id:1, trainer_id:1, trainee_id:1, duration:30 min, intensity:1, date:2025-9-1)"
        print("Test ExerciseSession passed")
        return True
    except Exception as error:
        print("Test ExerciseSession failed")  
        return False   

def testPTMS():
    try:
        system = PersonalTrainingManagementSystem()

        #Create multiple Trainers
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainer("T002", "Bob Coach") == True
        assert system.add_trainer("T003", "Charlie Mentor") == True

        #Create multiple Trainees
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.add_trainee("R101", "Evan Learner", date(2000,12,1), "evan@example.com") == True
        assert system.add_trainee("R102", "Faith Rookie", date(2002,7,22), "faith@example.com") == True

        #Create multiple Sessions
        assert system.create_session("S900", "T001", "R100", 60, 7, date(2025,8,1)) == True
        assert system.create_session("S901", "T001", "R100", 45, 8, date(2025,8,8)) == True
        assert system.create_session("S902", "T002", "R101", 30, 6, date(2025,8,5)) == True
        assert system.create_session("S903", "T002", "R101", 50, 9, date(2025,8,12)) == True
        assert system.create_session("S904", "T001", "R102", 40, 5, date(2025,8,20)) == True
        assert system.create_session("S905", "T003", "R100", 45, 8, date(2025,8,8)) == True

        #Test getter
        assert system.get_trainer("T001").__str__() == "Trainer(id:T001, name:Alice Trainer)"

        assert system.get_trainee("R100").__str__() == "Trainee(id:R100, name:Dana Trainee, birthdate:1998-3-15, email=:dana@example.com, age:27)"

        assert system.get_session("S900").__str__() == "ExerciseSession(id:S900, trainer_id:T001, trainee_id:R100, duration:60 min, intensity:7, date:2025-8-1)"

        assert system.get_trainee_total_duration("R100") == 150

        assert system.get_trainee_ave_intensity("R100") == 7.67

        assert system.get_trainer_total_duration("T001") == 145

        assert system.get_trainer_total_duration_with_trainee("T001","R100") == 105

        #test remove_session
        assert system.remove_session("S905") == True

        assert system.get_trainer_total_duration_with_trainee("T003","R100") == 0

        print("test PTMS passed")
        return True

    except AssertionError:
        print("test PTMS failed")
        return False


def checkAllVariablesArePrivate():
    global score
    try:
        birthdate = date(1999, 12, 1)
        t = Trainee(1,"John",birthdate,"abc@gmail.com")
        v = get_non_private_instance_variables(t)
        if(len(v)!=0):
            print("Trainee instant variable must be private")
        else:
            print("Trainee instant variables are all private")
            score += 1
    except Exception as error:
        print("Test Trainee private variables failed")   

    try:
        t = Trainer(1,"Peter")
        v = get_non_private_instance_variables(t)
        if(len(v)!=0):
            print("Trainer instant variable must be private")
        else:
            print("Trainer instant variables are all private")
            score += 1
    except Exception as error:
         print("Test Trainer private variables failed")

    try:
        session_date = date(2025, 9, 1)
        s = ExerciseSession(1,1,1,30,1,session_date)
        v = get_non_private_instance_variables(s)
        if(len(v)!=0):
            print("ExerciseSession instant variable must be private")
        else:
            print("ExerciseSession instant variables are all private")
            score += 1
    except Exception as error:
        print("Test ExerciseSession failed")  

    try:
        system = PersonalTrainingManagementSystem()
        v = get_non_private_instance_variables(system)
        if(len(v)!=0):
            print("PersonalTrainingManagementSystem instant variable must be private")
        else:
            print("PersonalTrainingManagementSystem instant variables are all private")
            score += 1
    except Exception as error:
         print("Test PersonalTrainingManagementSystem private variables failed")

def testPTMSErrorCase():
    global score

    #test duplicate trainer ID
    try:
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainer("T001", "Alice Trainer") == False
        score+=1
        print("Test PTMS test case 1 passed")
    except Exception:
        print("Test PTMS test case 1 failed")

    #empty trainer ID
    try:
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("", "Name") == False
        assert system.add_trainer(None, "Name") == False
        score+=1
        print("Test PTMS test case 2 passed")
    except Exception:
        print("Test PTMS test case 2 failed")

    #empty trainer name
    try:
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "") == False
        assert system.add_trainer("T001", None) == False
        score+=1
        print("Test PTMS test case 3 passed")
    except Exception:
        print("Test PTMS test case 3 failed")

    #duplicate Trainee ID
    try:
        system = PersonalTrainingManagementSystem()
        #Create multiple Trainees
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == False
        score+=1
        print("Test PTMS test case 4 passed")
    except Exception:
        print("Test PTMS test case 4 failed")
    
    #empty Trainee ID
    try:
        system = PersonalTrainingManagementSystem()
        #Create multiple Trainees
        assert system.add_trainee("", "Dana Trainee", date(1998,3,15), "dana@example.com") == False
        assert system.add_trainee(None, "Dana Trainee", date(1998,3,15), "dana@example.com") == False
        score+=1
        print("Test PTMS test case 5 passed")
    except Exception:
        print("Test PTMS test case 5 failed")

    #empty Trainee name
    try:
        system = PersonalTrainingManagementSystem()
        #Create multiple Trainees
        assert system.add_trainee("ID", "", date(1998,3,15), "dana@example.com") == False
        assert system.add_trainee("ID", None, date(1998,3,15), "dana@example.com") == False
        score+=1
        print("Test PTMS test case 6 passed")
    except Exception:
        print("Test PTMS test case 6 failed")


    #empty Trainee email
    try:
        system = PersonalTrainingManagementSystem()
        #Create multiple Trainees
        assert system.add_trainee("ID", "name", date(1998,3,15), "") == False
        assert system.add_trainee("ID", "name", date(1998,3,15), None) == False
        score+=1
        print("Test PTMS test case 7 passed")
    except Exception:
        print("Test PTMS test case 7 failed")

    #Empty Trainee birthdate
    try:
        system = PersonalTrainingManagementSystem()
        assert system.add_trainee("ID", "name", "", "test@email.com") == False
        assert system.add_trainee("ID", "name", None, "test@email.com") == False
        score+=1
        print("Test PTMS test case 8 passed")
    except Exception:
        print("Test PTMS test case 8 failed")


    #Invalid Trainee birthdate, future date
    try:
        system = PersonalTrainingManagementSystem()
        assert system.add_trainee("ID", "name", date(3000,3,15), "test@email.com") == False
        score+=1
        print("Test PTMS test case 9 passed")
    except Exception:
        print("Test PTMS test case 9 failed")

    #duplicate session ID
    try: 
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.create_session("S900", "T001", "R100", 60, 7, date(2025,8,1)) == True
        assert system.create_session("S900", "T001", "R100", 60, 7, date(2025,8,1)) == False
        score+=1
        print("Test PTMS test case 10 passed")
    except Exception:
        print("Test PTMS test case 10 failed")

    #invalid session Trainer ID
    try: 
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.create_session("S900", "T002", "R100", 60, 7, date(2025,8,1)) == False
        score+=1
        print("Test PTMS test case 11 passed")
    except Exception:
        print("Test PTMS test case 11 failed")

    #invalid session Trainee ID
    try: 
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.create_session("S900", "T001", "R102", 60, 7, date(2025,8,1)) == False
        score+=1
        print("Test PTMS test case 12 passed")
    except Exception:
        print("Test PTMS test case 12 failed")

    #invalid session duration (-ve, or non number)
    try: 
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.create_session("S900", "T001", "R100", -60, 7, date(2025,8,1)) == False
        assert system.create_session("S900", "T001", "R100", "a str", 7, date(2025,8,1)) == False
        score+=1
        print("Test PTMS test case 13 passed")
    except Exception:
        print("Test PTMS test case 13 failed")

    #invalid session intensity (1 to 10)
    try: 
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.create_session("S900", "T001", "R100", 60, -1, date(2025,8,1)) == False
        assert system.create_session("S900", "T001", "R100", 60, 11, date(2025,8,1)) == False
        score+=1
        print("Test PTMS test case 14 passed")
    except Exception:
        print("Test PTMS test case 14 failed")

    #empty session date
    try: 
        system = PersonalTrainingManagementSystem()
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.create_session("S900", "T001", "R100", 60, 1, "") == False
        assert system.create_session("S900", "T001", "R100", 60, 1, None) == False
        score+=1
        print("Test PTMS test case 15 passed")
    except Exception:
        print("Test PTMS test case 15 failed")

    try:
        system = PersonalTrainingManagementSystem()

        #Create multiple Trainers
        assert system.add_trainer("T001", "Alice Trainer") == True
        assert system.add_trainer("T002", "Bob Coach") == True
        assert system.add_trainer("T003", "Charlie Mentor") == True

        #Create multiple Trainees
        assert system.add_trainee("R100", "Dana Trainee", date(1998,3,15), "dana@example.com") == True
        assert system.add_trainee("R101", "Evan Learner", date(2000,12,1), "evan@example.com") == True
        assert system.add_trainee("R102", "Faith Rookie", date(2002,7,22), "faith@example.com") == True

        #Create multiple Sessions
        assert system.create_session("S900", "T001", "R100", 60, 7, date(2025,8,1)) == True
        assert system.create_session("S901", "T001", "R100", 45, 8, date(2025,8,8)) == True
        assert system.create_session("S902", "T002", "R101", 30, 6, date(2025,8,5)) == True
        assert system.create_session("S903", "T002", "R101", 50, 9, date(2025,8,12)) == True
        assert system.create_session("S904", "T001", "R102", 40, 5, date(2025,8,20)) == True
        assert system.create_session("S905", "T003", "R100", 45, 8, date(2025,8,8)) == True

        #invalid Trainee ID
        try:
            assert system.get_trainee_total_duration("R105") == False
            score+=3
            print("Test PTMS test case 16 passed")
        except Exception:
             print("Test PTMS test case 16 failed")

        
        #invalid Trainee ID
        try:
            assert system.get_trainee_ave_intensity("R105") == False
            score+=3
            print("Test PTMS test case 17 passed")
        except Exception:
             print("Test PTMS test case 17 failed")
        
        #invalid Trainer ID
        try:
            assert system.get_trainer_total_duration("T005") == False
            score+=3
            print("Test PTMS test case 18 passed")
        except Exception:
             print("Test PTMS test case 18 failed")
        
        #trainee not trained under trainer 
        try:
            assert system.get_trainer_total_duration_with_trainee("T001","R101") == 0
            score+=3
            print("Test PTMS test case 19 passed")
        except Exception:
             print("Test PTMS test case 19 failed")
        
        #invalid Trainer ID
        try:
            assert system.get_trainer_total_duration_with_trainee("T005","R100") == False
            score+=3
            print("Test PTMS test case 20 passed")
        except Exception:
             print("Test PTMS test case 20 failed")

        #invalid Trainee ID
        try:
            assert system.get_trainer_total_duration_with_trainee("T001","R105") == False
            score+=3
            print("Test PTMS test case 21 passed")
        except Exception:
             print("Test PTMS test case 21 failed")

        #test remove
        #invalid Session ID
        try:
            assert system.remove_session("S999") == False
            score+=3
            print("Test PTMS test case 22 passed")
        except Exception:
             print("Test PTMS test case 22 failed")
        
    except Exception:
        print("Test PTMS error case failed")
    
if __name__ == "__main__":
    #baseline test - all must pass
    state1,state2,state3,state4 = False,False,False,False
    
    state1 = testTrainee()
    if(state1):
        state2 = testTrainer()
    
    if(state2):
        state3 = testExerciseSession()
    
    if(state3):
        state4 = testPTMS()

    if(state4):
        #passline score
        score+=60
        checkAllVariablesArePrivate()
        testPTMSErrorCase()
    else:
        print("Base line testing StudentAssertiontest failed")
    
    score = round(score/100*10,2)
    print(f"Score:{score}")

        


