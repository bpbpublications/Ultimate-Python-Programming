class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items.pop()

    def display(self):
        print(self.items)

    def __iter__(self):
        return iter(self.items)


stack = Stack()
stack.push(20)
stack.push(30)
stack.push(10)
stack.push(89)

for item in stack:
    print(item)

print(min(stack), max(stack), sum(stack))
