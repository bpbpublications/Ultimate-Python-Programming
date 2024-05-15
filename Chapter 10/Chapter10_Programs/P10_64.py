def result(name, standard, **kwargs):
    total = sum(kwargs.values())
    per = total / len(kwargs)
    print(name, standard, kwargs)
    print(f'Total Marks = {total}, percentage={per}%')
    print('Pass' if per > 40 else 'Fail')


marks1 = {'Physics': 78, 'Maths': 34, 'Chemistry': 89}
marks2 = {'History': 89, 'Geography': 99}

result('Amit', 'VI', **marks1, **marks2)
