class OpenReadOnly:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.f = open(self.filename, 'r')
        return self.f

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()


with OpenReadOnly('test.txt') as file:
    print(file.read())
    print(file.write('xx'))  # will give error
