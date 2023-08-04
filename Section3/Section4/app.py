student = {"name": "Anitha", "grades": [70, 80, 90, 100]}

avg = lambda stu: sum(stu['grades']) / len(stu['grades'])

print(avg(student))


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


stu = Student('Anitha', [80, 90, 96, 100])

print(stu.average())


class Movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director


my_movie = Movie('The Matrix', 'Wachowski')

print(my_movie.name)