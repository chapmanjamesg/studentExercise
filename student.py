from NSSperson import NSSperson

class Student(NSSperson):
    def __init__(self, First_Name, Last_Name, Slack_Handle, Cohort):
        super().__init__(First_Name, Last_Name, Slack_Handle, Cohort)
        self.Exercises = list()