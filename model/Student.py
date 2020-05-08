# add . for relative path to curr dir
from .BasePerson import BasePerson

# inherit from BasePerson by adding arg to class definition
class Student(BasePerson):
    def __init__(self, name: str, school: str):
        # don't need to pass self when super()
        super().__init__(name)
        self.school = school

    def print_school(self):
        print(f"School is {self.school}")

    def say_hello(self):
        super().say_hello()

    # java's toString() equivalent
    # ref: https://youtu.be/f4iLWu_FP3M?t=516
    def __str__(self) -> str:
        return f"name={self.name}, school={self.school}"

