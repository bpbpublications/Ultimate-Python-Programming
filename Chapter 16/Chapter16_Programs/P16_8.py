class Teacher:
    def greet(self):
        print('I am a Teacher')


class Student:
    def greet(self):
        print('I am a Student')


class TeachingAssistant(Student, Teacher):
    pass


x = TeachingAssistant()
x.greet()
