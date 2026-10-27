class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class Student:
    def __init__(self, name):
        self.name = name

    def enroll(self, course):
        print(f"{self.name} enrolled in {course.course_name}")


course = Course("Python")
student = Student("Alex")

student.enroll(course)