import sys

fname = input('Enter name of the file : ')

while True:
    try:
        f = open(fname, 'r')
    except FileNotFoundError:
        print('File could not be found')
        fname = input('Enter the name of the file or x to exit : ')
        if fname == 'x':
            sys.exit()
    else:
        try:
            print(f.read())
        except OSError:
            print('Error in reading the file')
        finally:
            f.close()
            break
