from abc import ABC,abstractmethod
from datetime import date

class Session(ABC):
    session_counter = 1
    def __init__(self, patient, duration, base_rate):
        self.__session_id = Session.session_counter
        self.__patient = patient
        self.__duration = duration
        self.__base_rate = base_rate
        Session.session_counter += 1

    #Acessor method
    @property  
    def session_id(self):
        return self.__session_id

    @property
    def patient(self):
        return self.__patient

    @property
    def duration(self):
        return self.__duration

    @property
    def base_rate(self):
        return self.__base_rate
    
    @abstractmethod
    def calculate_cost(self):
        pass

#-----------------------------------------------------------------------------------------------------
#Subclass
class GeneralTherapy(Session):
    def __init__(self,patient, duration, base_rate, focus_area):
        super().__init__(patient, duration, base_rate)
        self.__focus_area = focus_area

    def calculate_cost(self):
        patient = self.patient
        duration = self.duration
        rate = self.base_rate
        
        base_cost = (duration / 30) * rate
        #Senior (60 years old and above) get a 20% discount on the total cost.
        if patient.getAge() >= 60:
            base_cost *= 0.8

        return round(base_cost,1)

#-----------------------------------------------------------------------------------------------------
#Subclass
class SportsInjury(Session):
    def __init__(self,patient, duration, base_rate, sport_type, injury_severity, pro_athlete):
        super().__init__(patient, duration, base_rate)
        self.__sport_type = sport_type
        self.__injury_severity = injury_severity
        self.__pro_athlete = pro_athlete

    def calculate_cost(self):
        patient = self.patient
        duration = self.duration
        rate = self.base_rate

        cost = (duration / 30) * rate
        #Senior (60 years old and above) get a 20% discount on the total cost.
        if patient.getAge() >= 60:
            cost = cost - (cost * 0.2)

        #Professional athlete get a 80% discount on the total cost.
        if self.__pro_athlete == True:
            cost = cost - (cost * 0.8)

        return round(cost,1)

#-----------------------------------------------------------------------------------------------------
#Subclass
class PostSurgeryRehab(Session):
    def __init__(self,patient, duration, base_rate,surgery_type):
        super().__init__(patient, duration, base_rate)
        self.__surgery_type = surgery_type

    def calculate_cost(self):
        patient = self.patient
        duration = self.duration
        rate = self.base_rate

        #Apply 15% surcharge to the base cost
        cost = (duration / 30) * rate
        cost = cost + (cost * 0.15)

        #Senior (60 years old and above) get a 20% discount on the total cost.
        if patient.getAge() >= 60:
            cost = cost - (cost * 0.2)

        return round(cost,1)

#-----------------------------------------------------------------------------------------------------
#Subclass
class PaediatricTherapy(Session):
    def __init__(self,patient, duration, base_rate,guardian_name):
        super().__init__(patient, duration, base_rate)
        self.__guardian_name = guardian_name

    def calculate_cost(self):
        patient = self.patient
        duration = self.duration
        rate = self.base_rate   

        #Apply 10% discount to the base cost
        cost = (duration / 30) * rate
        cost = cost - (cost * 0.10)

        #Senior (60 years old and above) get a 20% discount on the total cost.
        if patient.getAge() >= 60:
            cost = cost - (cost * 0.2)

        return round(cost,1)

#-----------------------------------------------------------------------------------------------------
class Patient:
    patient_counter = 1

    def __init__(self,name,birthdate):
        self.__patient_id = Patient.patient_counter
        self.__name = name
        self.__birthdate = birthdate
        Patient.patient_counter += 1

    #Accessor method
    @property
    def patient_id(self):
        return self.__patient_id

    @property
    def name(self):
        return self.__name

    @property
    def birthdate(self):
        return self.__birthdate

    #Mutator method

    def getAge(self):
        today = date.today()
        age = today.year - self.__birthdate.year
        if (today.month, today.day) < (self.__birthdate.month, self.__birthdate.day):
            age -= 1

        return age
             
    def __str__(self):
        return f'Patient(id:{self.__patient_id}, name:{self.__name}, age:{self.getAge()})'

    def __eq__(self, other):
        return (self.__patient_id == other.__patient_id)

#-----------------------------------------------------------------------------------------------------
class ClinicBookingSystem:
    def __init__(self):
        #Empty dictionaries
        self.__patients = {}
        self.__sessions = {}

    def add_patient(self, name, birthdate):
        try:
            patient = Patient(name, birthdate)
            self.__patients[patient.patient_id] = patient
            self.__sessions[patient.patient_id] = []    #Empty list
            return patient.patient_id
        except Exception:
            return False

    #Accessor method
    def get_patient(self, patient_id):
        return self.__patients.get(patient_id, False)

    def get_sessions(self, patient_id):
        if patient_id not in self.__sessions:
            return False
        return self.__sessions[patient_id]

    def book_session(self, session_type, patient_id, duration, base_rate, **kwargs):
        try:
            patient = self.get_patient(patient_id)
            if not patient:
                return False

            session = None

            if session_type == "General":
                session = GeneralTherapy(patient, duration, base_rate, kwargs.get("focus_area"))

            elif session_type == "Sports":
                session = SportsInjury(patient, duration, base_rate,
                                       kwargs.get("sport_type"),
                                       kwargs.get("injury_severity"),
                                       kwargs.get("pro_athlete"))

            elif session_type == "PostSurgery":
                session = PostSurgeryRehab(patient, duration, base_rate, kwargs.get("surgery_type"))

            elif session_type == "Paediatric":
                if patient.getAge() > 18:
                    return False
                session = PaediatricTherapy(patient, duration, base_rate, kwargs.get("guardian_name"))
            else:
                return False

            if not session:
                return False

            self.__sessions[patient_id].append(session)
            return True

        except Exception:
            return False