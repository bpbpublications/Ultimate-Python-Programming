class CM():

    def __init__(self, name):
        print('__init__ called')
        self.name = name

    def __enter__(self):
        print('__enter__ called')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit__ called')

    def do_something(self):
        print('Something is being done')


with CM('xyz'):
    print('Hello')
    print(15 / 3)
    print('Bye')
