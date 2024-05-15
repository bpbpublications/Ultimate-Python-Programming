class File():
    def __init__(self, filename='test.txt', mode='a'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with File() as f:
    f.write('xxx')

with File('log.txt') as f:
    f.write('ccc')

with File('data.txt', 'r') as f:
    print(f.read())
