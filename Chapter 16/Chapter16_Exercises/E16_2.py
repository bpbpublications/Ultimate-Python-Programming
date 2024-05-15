class Mother:
    def cook(self):
        print('Can cook pasta')


class Father:
    def cook(self):
        print('Can cook noodles')


class Daughter(Father, Mother):
    pass


class Son(Mother, Father):
    def cook(self):
        super().cook()
        print('Can cook butter chicken')


d = Daughter()
s = Son()

d.cook()
print()
s.cook()
