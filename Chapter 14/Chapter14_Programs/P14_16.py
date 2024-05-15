class Product:
    def __init__(self):
        self.data1 = 10
        self.__data2 = 20

    def method1(self):
        print('Executing method1')

    def __method2(self):
        print('Executing method2')


p = Product()
print(p.data1, p.__data2)
p.method1()
p.__method2()
