for filename in ['data.txt', 'data11.txt', 'data2.txt', 'text.txt']:
    try:
        f = open(filename, 'r')
    except OSError:
        print(f'{filename} could not be opened')
    else:
        try:
            print(f'{filename} has {len(f.read())} characters')
        finally:
            f.close()
