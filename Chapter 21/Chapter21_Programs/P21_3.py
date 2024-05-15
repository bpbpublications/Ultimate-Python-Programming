class CM():

    def __init__(self, name):
        print('__init__called')
        self.name = name

    def __enter__(self):
        print('__enter__called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit__called')

    def do_something(self):
        print('Something is being done')


with CM('xyz') as c:
    print('Hello')
    print(15 / 3)
    print('Bye')
    print(c)
    print(c.name)
    c.do_something()
