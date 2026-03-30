from datetime import datetime,date
class Trainee:
	def __init__(self, trainee_id, name, birthdate, email):
		self.__trainee_id = trainee_id
		self.__name = name
		self.__birthdate = birthdate
		self.__email = email

	def get_age(self):
		today = date.today()
		age = today.year - self.__birthdate.year

		if (today.month,today.day) < (self.__birthdate.month,self.__birthdate.day):
			age -= 1
		return age

	def __str__(self):
		birthdate_str = f"{self.__birthdate.year}-{self.__birthdate.month}-{self.__birthdate.day}"
		return f"Trainee(id:{self.__trainee_id}, name:{self.__name}, birthdate:{birthdate_str}, email=:{self.__email}, age:{self.get_age()})"


class Trainer:
	def __init__(self, trainer_id, name):
		self.__trainer_id = trainer_id
		self.__name = name

	def __str__(self):
		return f'Trainer(id:{self.__trainer_id}, name:{self.__name})'

class ExerciseSession:
	def __init__(self, session_id, trainer_id, trainee_id, duration, intensity, date):
		self.__session_id = session_id
		self.__trainer_id = trainer_id
		self.__trainee_id = trainee_id
		self.__duration = duration
		self.__intensity = intensity
		self.__date = date

	def __str__(self):
		date_str = f"{self.__date.year}-{self.__date.month}-{self.__date.day}"
		return f'ExerciseSession(id:{self.__session_id}, trainer_id:{self.__trainer_id}, trainee_id:{self.__trainee_id}, duration:{self.__duration} min, intensity:{self.__intensity}, date:{date_str})'

class PersonalTrainingManagementSystem:
	def __init__(self):
		self.__trainers = []
		self.__trainees = []
		self.__sessions = []

	def add_trainer(self,ID,name):
		i = Trainer(ID,name)
		if i in self.__trainers:
			return False
		else:
			self.__trainers.append(i)
			return True

	def add_trainee(self,ID,name,birthdate,email):
		k = Trainee(ID,name,birthdate,email)
		if k in self.__trainees:
			return False
		else:
			self.__trainees.append(k)
			return True

	def create_session(self,ID,trainer_id,trainee_id,duration,intensity,date):
		j = ExerciseSession(ID,trainer_id,trainee_id,duration,intensity,date)
		if j in self.__sessions:
			return False
		else:
			self.__sessions.append(j)
			return True

	def get_trainer(self,trainer_id):
		for trainer in self.__trainers:
			if trainer._Trainer__trainer_id == trainer_id:
				return trainer
		return None

	def get_trainee(self,trainee_id):
		for trainee in self.__trainees:
			if trainee._Trainee__trainee_id == trainee_id:
				return trainee
		return None

	def get_session(self,session_id):
		for session in self.__sessions:
			if session._ExerciseSession__session_id == session_id:
				return session
		return None

	def get_trainee_total_duration(self,trainee_id):
		total = 0
		for session in self.__sessions:
			if session._ExerciseSession__trainee_id == trainee_id:
				total += session._ExerciseSession__duration
		return total

	def get_trainee_ave_intensity(self,trainee_id):
		total = 0
		sessnum = 0
		for session in self.__sessions:
			if session._ExerciseSession__trainee_id == trainee_id:
				total += session._ExerciseSession__intensity
				sessnum += 1
		if sessnum == 0:
			return 0
		else:
			avg = round(total /sessnum,2)
			return avg


	def get_trainer_total_duration(self,trainer_id):
		total = 0
		for session in self.__sessions:
			if session._ExerciseSession__trainer_id == trainer_id:
				total += session._ExerciseSession__duration
		return total

	def get_trainer_total_duration_with_trainee(self,trainer_id,trainee_id):
		total = 0
		for session in self.__sessions:
			if (session._ExerciseSession__trainer_id == trainer_id and session._ExerciseSession__trainee_id == trainee_id):
				total += session._ExerciseSession__duration
		return total

	def remove_session(self,session_id):
		for session in self.__sessions:
			if session._ExerciseSession__session_id == session_id:
				self.__sessions.remove(session)
				return True
		return False