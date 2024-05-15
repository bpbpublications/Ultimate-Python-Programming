class Test:
    def method1(self, x):
        self.x = x

    def method2(self):
        x += 10

    def display(self):
        print(self.x)


t = Test()
t.method1(5)
t.method2()
t.display()
