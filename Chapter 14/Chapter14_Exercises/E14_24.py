class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(self.title)
        print(f'ISBN : {self.isbn}')
        print(f'Price : {self.price}')
        print(f'Number of copies : {self.copies}')
        print('.' * 50)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 10 <= new_price <= 500:
            self._price = new_price
        else:
            raise ValueError('Price cannot be less than 10 or more than 500')


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 222200, 20)

book1.display()
book2.display()

