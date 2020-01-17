class Cohort():
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def add_students(self, student):
        self.students.append(student)
        student.cohort = self.name

    def add_instructors(self, instructor):
        self.instructors.append(instructor)
        instructor.cohort = self.name
