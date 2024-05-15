try:
    File = open('datafile.txt')
except OSError as err:
    for entry in dir(err):
        if not entry.startswith("_"):
            try:
                print(entry, "=", err.__getattribute__(entry))
            except AttributeError:
                pass
