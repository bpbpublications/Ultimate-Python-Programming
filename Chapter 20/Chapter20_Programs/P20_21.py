try:
    file = open('datafile.txt')
except OSError as err:
    for entry in dir(err):
        if not entry.startswith("_"):
            print(entry, "=", err.__getattribute__(entry))
