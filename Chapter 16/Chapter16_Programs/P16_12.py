class Person:
    def greet(self):
        print('I am a Person')


class Teacher(Person):
    def greet(self):
        super().greet()
        print('I am a Teacher')


class Student(Person):
    def greet(self):
        super().greet()
        print('I am a Student')


class TeachingAssistant(Student, Teacher):
    def greet(self):
        super().greet()
        print('I am a Teaching Assistant')


x = TeachingAssistant()
x.greet()
print()
s = Student()
s.greet()

print(help(TeachingAssistant))
print(help(Student))