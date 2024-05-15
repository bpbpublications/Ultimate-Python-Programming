def func():
    try:
        f = open('xyz')
    except Exception as e:
        print('An exception occurred', e)
        raise


print('Start')

try:
    func()
except FileNotFoundError as e:
    print('Caught a FileNotFoundError', e)
    print('Handling the error')
print('End')
