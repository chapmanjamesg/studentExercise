from NSSperson import NSSperson

class Instructor(NSSperson):
    def __init__(self, first_name, last_name, slack_handle, specialty):
        super().__init__(first_name, last_name, slack_handle)
        self.cohort = ""
        self.specialty = specialty
    
    def assign_exercise(self, exercise, cohort):
        for student in cohort.students:
            student.exercises.append(exercise)

