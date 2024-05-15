try:
    file = open('ff')
except OSError as err:
    print(type(err))
    print(err.args)
