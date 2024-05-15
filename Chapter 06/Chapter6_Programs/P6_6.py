athletes = ['Ram', 'Sam', 'Shyam', 'Abhi', 'Adi']
student = input('Enter student name : ')
if student in athletes:
    print('You are awarded a scholarship')

failed_students = ['Pam', 'Sam', 'Ron', 'Ted']
student = input('Enter  student name: ')
if student not in failed_students:
    print('You are promoted')
