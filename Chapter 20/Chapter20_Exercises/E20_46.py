students = {'Raj': [80, 60, 70], 'Deep': [80, 90], 'Ron': [], 'Sam': [70, 50]}
try:
    for name in students.keys():
        average_marks = sum(students[name]) / len(students[name])
        print(name, average_marks)
except ZeroDivisionError:
    pass
print('End')



students = {'Raj': [80, 60, 70], 'Deep': [80, 90], 'Ron': [], 'Sam': [70, 50]}
for name in students.keys():
    try:
        average_marks = sum(students[name]) / len(students[name])
        print(name, average_marks)
    except ZeroDivisionError:
        pass

print('End')
