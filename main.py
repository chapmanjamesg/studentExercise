from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

tommy = Student("Tommy", "Oliver", "OGWhiteRanger")
billy = Student("Billy", "Cranston", "TriSaratops")
kim = Student("Kimberly", "Hart", "pinkCheer")
jason = Student("Jason", "Scott", "RedBeatsWhite")
zack = Student("Zack", "Taylor", "danceTillYouDrop")
trini = Student("Trini", "Kwan", "heartBreaker")

zordon = Instructor("Zordon", "Redacted", "itsMorphinTime1", "turning children to solders")
alpha5 = Instructor("Alpha5", "Robot", "betterThenZordon", "caretaker")
rita = Instructor("Rita", "Repulsa", "moon4thewin", "making people bigger")

ninety_three = Cohort("Cohort 93")
ninety_three.add_students(billy)
ninety_three.add_students(kim)
ninety_three.add_instructors(zordon)
ninety_four = Cohort("Cohort 94")
ninety_four.add_students(tommy)
ninety_four.add_students(jason)
ninety_four.add_instructors(alpha5)
ninety_five = Cohort("Cohort 95")
ninety_five.add_students(zack)
ninety_five.add_students(trini)
ninety_five.add_instructors(rita)

puddy_buddy = Exercise("Puddy Buddy", "JavaScript")
morphin_time = Exercise("Morphin Time", "HTML/CSS")
calling_zords = Exercise("Call your Zords instructions", "JSON server")
megazord_formation = Exercise("Form the Megazord", "Python")


zordon.assign_exercise(puddy_buddy, ninety_three)
zordon.assign_exercise(megazord_formation, ninety_three)
alpha5.assign_exercise(morphin_time, ninety_four)
alpha5.assign_exercise(calling_zords, ninety_four)
rita.assign_exercise(puddy_buddy, ninety_five)
rita.assign_exercise(morphin_time, ninety_five)

print(tommy.last_name)