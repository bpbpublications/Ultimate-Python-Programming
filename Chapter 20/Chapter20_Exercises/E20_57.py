def read_files(filenames):
    for filename in filenames:
        f = None
        try:
            f = open(filename)
            print(f.read())
        except(OSError, ValueError):
            pass
        finally:
            if f is not None:
                f.close()


filesList = ['data1.txt', 'data.txt', 'data3.txt', 'data4.txt']
read_files(filesList)
