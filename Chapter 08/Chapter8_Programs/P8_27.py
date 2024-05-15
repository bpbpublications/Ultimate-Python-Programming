while True:
    student_id = int(input('Enter student id :'))
    if 1000 < student_id < 5000:
        break
    print('Invalid id : id should be a number between 1000 and 5000')
