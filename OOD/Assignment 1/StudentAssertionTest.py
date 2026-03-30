#rename your python file as A1.py and test your Assignment
from A1 import Trainee,Trainer,ExerciseSession,PersonalTrainingManagementSystem
from datetime import datetime, date

def testTrainee():
    try:
        birthdate = date(1999, 12, 1)
        t = Trainee(1,"John",birthdate,"abc@gmail.com")
        age = t.get_age()
        assert age==25
        assert t.__str__() == "Trainee(id:1, name:John, birthdate:1999-12-1, email=:abc@gmail.com, age:25)"
        print("testTrainee passed")
    except AssertionError as error:
        print("testTrainee failed")    
    
def testTrainer():
    try:
        t = Trainer(1,"Peter")
        assert t.__str__() == "Trainer(id:1, name:Peter)"
        print("testTrainer passed")  
    except AssertionError as error:
        print("testTrainer failed")
    
def testExerciseSession():
    try:
        session_date = date(2025, 9, 1)
        s = ExerciseSession(1,1,1,30,1,session_date)
        assert s.__str__() == "ExerciseSession(id:1, trainer_id:1, trainee_id:1, duration:30 min, intensity:1, date:2025-9-1)"
        print("testExerciseSession passed")  
    except AssertionError as error:
        print("testExerciseSession failed")     

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

        #test remove
        assert system.remove_session("S905") == True

        assert system.get_trainer_total_duration_with_trainee("T003","R100") == 0

        print("testPTMS passed")

    except AssertionError:
        print("testPTMS failed")

if __name__ == "__main__":

    testTrainee();
    testTrainer();
    testExerciseSession();
    testPTMS();
        


