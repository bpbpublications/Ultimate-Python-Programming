def result(name, standard, **kwargs):
    total = sum(kwargs.values())
    per = total / len(kwargs)
    print(name, standard, kwargs)
    print(f'Total Marks = {total}, percentage={per:.2f}%')
    print('Pass' if per > 40 else 'Fail')


result('Amit', 'VI', physics=89, maths=45)
result('Anuj', 'V', physics=89, maths=45, chemistry=90, history=87)

marks = {'Physics': 78, 'Maths': 34, 'Chemistry': 89}
result('Amit', 'VI', **marks)

marks1 = {'Physics': 78, 'Maths': 34, 'Chemistry': 89, 'History': 89, 'Geography': 99}
result('Amit', 'VI', **marks1)
