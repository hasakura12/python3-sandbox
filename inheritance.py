
from model.BasePerson import BasePerson
from model.Student import Student

print()
print("~WORKING ON BasePerson class...")
person = BasePerson(name = "Arthur")
person.say_hello()

student = Student(name = "Aristotle", school = "Greek")
student.print_school()
student.say_hello()

# this will call Java's toString() equivalent of __str__()
print(student)