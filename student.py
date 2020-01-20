from NSSperson import NSSperson

class Student(NSSperson):
    def __init__(self, first_name, last_name, slack_handle):
        super().__init__(first_name, last_name, slack_handle)
        self.cohort = ""
        self.exercises = list()