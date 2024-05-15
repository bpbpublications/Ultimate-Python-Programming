class MyClass:

    @classmethod
    def method1(cls):
        print('method1 doing work')
        cls.method2()
        cls.method3()

    @staticmethod
    def method2():
        print('method2 doing work')

    @staticmethod
    def method3():
        print('method3 doing work')

MyClass.method1()