class Cart:
    def __init__(self):
        self.grocery_items = []
        self.stationery_items = []

    def add_stationery(self, item, quantity=1):
        self.grocery_items.append((item, quantity))

    def add_grocery(self, item, quantity=1):
        self.stationery_items.append((item, quantity))

    def __iter__(self):
        return CartIterator(self)


class CartIterator:
    def __init__(self, source):
        self.source = source
        self.i = 0

    def __next__(self):
        if self.i >= (len(self.source.grocery_items) + len(self.source.stationery_items)):
            raise StopIteration
        if self.i < len(self.source.grocery_items):
            item = self.source.grocery_items[self.i]
        else:
            item = self.source.stationery_items[self.i - len(self.source.grocery_items)]
        self.i += 1
        return item


cart = Cart()

cart.add_grocery('rice')
cart.add_stationery('pen', 3)
cart.add_stationery('eraser')
cart.add_stationery('pencil', 5)
cart.add_grocery('bread', 2)
cart.add_grocery('pasta')

for item, quantity in cart:
    print(item, quantity)
