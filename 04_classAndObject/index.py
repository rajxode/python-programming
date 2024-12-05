# from "fileName" import "className"
from StudentClass import Student
from UserClass import User
from AdminClass import Admin

student1 = Student("Baburao", 2, False, 73)

print("Name: " + student1.name)
print("Roll No.: " + str(student1.roll_no))
print("Is student present: " + str(student1.is_present))
print("Student's percentage: " + str(student1.percentage))
print("Student's grade: " + (student1.get_grade()))

user1 = User()
admin1 = Admin()

print(user1.say_hello())
print(admin1.say_hello())
print("\n")
print(user1.say_hello_world())
print(admin1.say_hello_world())
