def result(m1, m2, m3, m4):
    total = m1 + m2 + m3 + m4
    per = total / 4
    print(f'Total Marks = {total}, percentage={per}%')
    print('Pass' if per > 40 else 'Fail')


result(56, 89, 77, 67)

marks = [93, 34, 54, 67]
result(marks[0], marks[1], marks[2], marks[3])
result(*marks)

marks = [93, 34, 54, 67, 56, 89]
result(*marks[:4])
