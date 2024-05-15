def result(*args, grade=False):
    total = sum(args)
    per = total / len(args)
    print(f'Total Marks = {total}, percentage = {per}%')
    if grade == False:
        return
    if per > 80:
        print('Grade A')
    elif per > 50:
        print('Grade B')
    else:
        print('Grade C')

result(90, 90, 90, grade=True)
result(90, 90, 90, True)
