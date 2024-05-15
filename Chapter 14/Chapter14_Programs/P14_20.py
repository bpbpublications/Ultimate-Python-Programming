class Stack:
    MAX_LIMIT = 10

    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) >= Stack.MAX_LIMIT:
            raise Exception('Stack is full')
        self.items.append(item)

    def pop(self):
        if self.items == []:
            raise RuntimeError('Stack is empty')
        return self.items.pop()

    def display(self):
        print(self.items)
