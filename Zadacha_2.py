class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.grades = list()

    def average_grade(self):
        if not self.grades:
            print('Ошибка!')
        else:
            print(sum(self.grades)/len(self.grades))

    def add_grade(self, grade):
        self.grades.append(grade)
