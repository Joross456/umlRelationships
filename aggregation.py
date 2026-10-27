class Teacher:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, teachers):
        self.teachers = teachers


teacher1 = Teacher("John")
teacher2 = Teacher("Mary")

department = Department([teacher1, teacher2])

for teacher in department.teachers:
    print(teacher.name)