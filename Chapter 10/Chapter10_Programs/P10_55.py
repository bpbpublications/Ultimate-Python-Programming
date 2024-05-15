def result(*args):
    print(args)
    total = sum(args)
    per = total / len(args)
    print(f'Total Marks = {total}, percentage={per:.2f}%')
    print('Pass' if per > 40 else 'Fail')


result(23, 89, 77, 67, 89, 90)
result(67, 83, 68)
result(89)
