class Student():
    def __init__(self, first_name, last_name, slack_handles):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handles
        self.cohort = ""
        self.exercises = list()