def result(name, standard, *args):
    print(name, standard)
    print(args)
    total = sum(args)
    per = total / len(args)
    print(f'Total Marks = {total}, percentage={per:.2f}%')
    print('Pass' if per > 40 else 'Fail')


result('Anu', 'VI', 34, 66, 88, 99, 344)
result('Dev', 'V', 99, 344)

marks1 = [23, 45, 67]
marks2 = [23, 45, 67, 89, 88, 99]
marks3 = [56, 77, 88, 22, 77]

result('Anu', 'VI', *marks1)
result('Anu', 'VI', *marks2)
result('Anu', 'VI', *marks3)
