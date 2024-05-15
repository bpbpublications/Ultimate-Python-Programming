def func():
    def g():
        print('Hello')

    return g()


g()
