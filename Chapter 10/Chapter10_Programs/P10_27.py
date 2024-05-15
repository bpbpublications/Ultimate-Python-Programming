data = {}


def enter_data(d):
    while True:
        id = input('Enter id (0 to quit): ')
        if id == '0':
            break
        name = input('Enter name : ')
        d[id] = name


enter_data(data)
print(data)
