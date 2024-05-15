class Teacher:
    def greet(self):
        print('I am a Teacher')


class Student:
    def greet(self):
        print('I am a Student')


class TeachingAssistant(Teacher, Student):
    pass


x = TeachingAssistant()
x.greet()

print(TeachingAssistant.__bases__)