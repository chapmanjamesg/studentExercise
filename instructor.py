from NSSperson import NSSperson

class Instructor(NSSperson):
    def __init__(self, First_Name, Last_Name, Slack_Handle, Specialty, Cohort):
        super().__init__(First_Name, Last_Name, Slack_Handle, Cohort)
        self.Specialty = Specialty
    
    def assign_exercise(self, Exercise, Cohort):
        for Student in Cohort.Students:
            Student.Exercises.append(Exercise)

