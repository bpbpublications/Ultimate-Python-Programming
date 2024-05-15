students = {'Raj': [80, 60, 70], 'Deep': [80, 90], 'Ron': [], 'Sam': [70, 50]}

while True:
    try:
        name = input('Enter student name : ')
        average_marks = sum(students[name]) / len(students[name])
        print(name, average_marks)
        break
    except KeyError:
        print('Invalid name')
    except ZeroDivisionError:
        print('No marks available for this student')
        break
print('End')
