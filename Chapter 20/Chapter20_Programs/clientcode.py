import myfile

print('Start')

try:
    myfile.func1()
    print('End')
except myfile.DatabaseError as e:
    print(type(e))
print('End')
