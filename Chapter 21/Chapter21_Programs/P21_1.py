class CM():
    def __enter__(self):
        print('__enter__called')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit__called')


with CM():
    print('Hello')
    print(15 / 3)
    print('Bye')
