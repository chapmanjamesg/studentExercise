class Cohort():
    def __init__(self, Name):
        self.Name = Name
        self.Students = list()
        self.Instructors = list()

    def add_students(self, Student):
        self.Students.append(Student)
        Student.Cohort = self.Name

    def add_instructors(self, Instructor):
        self.Instructors.append(Instructor)
        Instructor.Cohort = self.Name
