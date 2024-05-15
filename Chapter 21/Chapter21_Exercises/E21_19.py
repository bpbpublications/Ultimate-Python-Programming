class Indenter:
    def __init__(self, spaces=2):
        self.spaces = spaces

    def __enter__(self):
        global print
        self.original_print = print
        print = self.print

    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self.original_print

    def print(self, text):
        self.original_print(' ' * self.spaces + str(text))


print('Welcome')

with Indenter(4):  # indented by 4 spaces
    print('Hello')
    L = [1, 2]
    print(L)

print('Python')

with Indenter(8):  # indented by 8 spaces
    print('Hi')
    x = 5
    y = 7
    print(x + y)

with Indenter():  # By default, indented by 2 spaces
    print('Programming')

print('Bye')
