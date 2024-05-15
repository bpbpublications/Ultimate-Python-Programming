name = input('Enter name : ')
marks_maths = int(input('Enter marks in maths : '))
marks_physics = int(input('Enter marks in physics : '))
marks_chemistry = int(input('Enter marks in chemistry : '))

total_marks = marks_maths + marks_physics + marks_chemistry
percentage = (total_marks / 300) * 100
print(name, percentage)
