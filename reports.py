import sqlite3
from student import Student
from cohort import Cohort

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/users/chapm/workspace/backend/python/exercises/studentExercises/studentexercise.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row:Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Student_Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.name
            from Student s
            join Cohort c on s.Cohort_Id = c.Cohort_Id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(f'{student.First_Name} {student.Last_Name} is in {student.Cohort}')
    
    
    def all_cohorts(self):

        """Retrieve all cohort"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row:Cohort(
                row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Cohort_Id,
                c.Name
            from Cohort c
            order by c.Cohort_Id
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort.Name)

reports = StudentExerciseReports()
# reports.all_students()
reports.all_cohorts()