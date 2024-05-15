class Teacher:
    def greet(self):
        print('I am a Teacher')


class Student:
    def greet(self):
        print('I am a Student')


class TeachingAssistant(Student, Teacher):
    def greet(self):
        print('I am a Teaching Assistant')

x = TeachingAssistant()
x.greet()
