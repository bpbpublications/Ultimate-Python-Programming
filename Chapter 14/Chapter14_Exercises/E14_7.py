class Test:
    def method1(self):
        print('Inside method1')

    def method2(self):
        print('Inside method2')
        method1()


t = Test()
t.method2()
