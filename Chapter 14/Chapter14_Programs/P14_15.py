class Product:
    def __init__(self):
        self.data1 = 10
        self._data2 = 20

    def method1(self):
        print('Executing method1')

    def _method2(self):
        print('Executing method2')


p = Product()
print(p.data1, p._data2)
p.method1()
p._method2()
