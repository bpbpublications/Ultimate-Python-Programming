class FileWriteOnly:

    def __init__(self, filename='test.txt'):
        self.filename = filename

    def __enter__(self):
        self.f = open(self.filename, 'w')
        return self.f

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()


with FileWriteOnly() as f:
    f.write('Hello')
