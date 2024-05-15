class CM():

    def __init__(self, name):
        print('__init__called')
        self.name = name

    def __enter__(self):
        print('__enter__called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit__called')

    def f(self):
        print('f called')


with CM('ABC') as c:
    print(c.name)
    print(10 % 2)
    c.f()

with CM('LMN') as c:
    print(c.name)
    print(10 % 0)
    c.f()
