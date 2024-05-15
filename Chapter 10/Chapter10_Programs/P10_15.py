def result(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    percentage = total / 3
    print(total, percentage)
    return 'Pass' if total > 100 else 'Fail'


r = result(88, 96, 46)  # return value used
print(r)
result(78, 45, 89)  # return value ignored
