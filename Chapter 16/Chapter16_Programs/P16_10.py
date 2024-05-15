class Person:
    def greet(self):
        print('I am a Person')


class Teacher(Person):
    def greet(self):
        print('I am a Teacher')


class Student(Person):
    def greet(self):
        print('I am a Student')


class TeachingAssistant(Student, Teacher):
    def greet(self):
        print('I am a Teaching Assistant')


print(help(TeachingAssistant))
print('---------------------------')
print(TeachingAssistant.__mro__)
print(TeachingAssistant.mro())

x = TeachingAssistant()
print(x.__class__.__mro__)
