import statistics as stats

class TestResultExecption(Exception):
    def __init__(self, message):
        super().__init__(message)

class TestResult:
    def __init__(self):
        self.__name = ""
        self.__scores = []

    def load(self,datafile_name):

        error_messages = []
        with open(datafile_name) as data_file:
            line_counter = 0
            for line in data_file:
                line_counter += 1
                #init the test name and skip
                if (line_counter == 1):
                    self.__name = line.strip()
                    continue
                data = line.split(",")
                id = data[0].strip()
                score = data[1].strip()
                if TestResult.__validate_score(score):
                    self.__scores[id] = int(score)
                else:
                    error_message = f"Invalid test score"
                    error_message.append(error_message)
        if (len(error_messages) != 0):
            delimiter = "\n"
            exception_message = delimiter.join(error_messages)
            raise TestResultExecption(exception_message)
    @staticmethod
    def __validate_score(score):
        if not score.isnumeric():
            return False
        score = float(score)
        if score < 0 or score > 100:
            return False
        return True
    
    def __validate_id(self,id):
        if id not in self.__scores:
            return False
        return True
    
    def __get_pass_count(self):
        pass_count = 0
        for id in self.__scores:
            score = self.__scores[id]
            if (score >= 50):
                pass_count += 1
        return pass_count
    
    def update_score(self,id,score):
        #check if id in keys
        if (not self.__validate_id(id)):
            raise TestResultExecption(f"Invalid student id: {id}")
        if TestResult.__validate_score(str(score)):
            self.__scores[id] = score
        else:
            raise TestResultExecption(f"Invalid test score: {score}")
        
    def get_score(self,id):
        if (not self.__validate_id(id)):
            raise TestResultExecption(f"Invalid student id: {id}")
        return self.__scores[id]
    
    def get_basic_states(self):
        score_list = self.__scores.value()
        highest = max(score_list)
        lowest = min(score_list)
        average = stats.mean(score_list)
        return highest,lowest,round(average,2)
    
    def get_retest_list(self):
        with open("retest_list.csv", "w") as retest_list:
            for id in self.__scores:
                score = self.__scores[id]
                if (score < 50):
                    retest_list.write(f"{id},{score}\n")
                
    def __str__(self):
        return f"Test name: {self.__name}, Pass count: {self.__get_pass_count()}"
    
def main():
    ts = TestResult()
    print("Test invalid data in csv")
    try:
        ts.load("data.csv")
    except TestResultExecption as ex:
        print(ex)
    print('#'*20)
    print("Test update_score() with Invalid student id")
    try:
        ts.load("data2.csv")
        ts.update_score("A",20)
    except TestResultExecption as ex:
        print(ex)
    print('#'*20)
    print("Test update_score() with invalid score")
    try:
        ts.load("data2.csv")
        ts.update_score("c1","XX")
    except TestResultExecption as ex:
        print(ex)
    print('#'*20)
    print("Test update_score() with a valid student id and score")
    try:
        ts.load("data2.csv")
        ts.update_score("c1",90)
        score = ts.get_score("c1")
        print(score)
    except TestResultExecption as ex:
        print(ex)
    print('#'*20)
    print("Test get_basic_stats()")
    highest,lowest,average = ts.get_basic_states()
    print(f"Highest:{highest},Lowest:{lowest},Average: {average}")
    print('#'*20)
    print("Test get_retest_list()")
    ts.get_retest_list()
    print('#'*20)
    print("Test str()")
    print(ts)

if __name__ == "__main__":
    main()