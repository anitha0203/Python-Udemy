class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


# class WorkingStudent:
#     def __init__(self, name, school, salary):
#         self.name = name
#         self.school = school
#         self.marks = []
#         self.salary = salary
#
#     def average(self):
#         return sum(self.marks) / len(self.marks)


#                                ORRRRRRRRRRRRRRRRRR


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)
print(rolf.weekly_salary)


class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters')

another_object = Bar()
another_object.hi()