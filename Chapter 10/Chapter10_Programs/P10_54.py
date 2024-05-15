marks2 = {'m1': 93, 'm2': 34, 'm3': 54, 'm4': 67}


def result(m1, m2, m3, m4):
    total = m1 + m2 + m3 + m4
    per = total / 4
    print(f'Total Marks = {total}, percentage={per}%')
    print('Pass' if per > 40 else 'Fail')


result(**marks2)
