from datetime import date

class Person:
    def __init__(self, name, y, m, d, address, phone):
        self.name = name
        self.address = address
        self.date_of_birth = date(y, m, d)
        self.phone = phone

    def contact_details(self):
        print(self.address, self.phone)

    @property
    def age(self):
        return (date.today() - self.date_of_birth).days // 365


class Book:
    def __init__(self, title, pages, y, m, d, author):
        self.title = title
        self.pages = pages
        self.publishing_date = date(y, m, d)
        self.author = author

    def display(self):
        print(f'{self.title} published in {self.publishing_date.year}, ', end='')
        print(f'written by {self.author.name}')

    def author_details(self):
        print(f'Author name : {self.author.name}, age : {self.author.age}')
        self.author.contact_details()

    def __lt__(self, other):
        return (self.publishing_date) < (other.publishing_date)


author1 = Person('Devank', 2010, 4, 29, '122 Madhi Nath', 998998987)
author2 = Person('Devanshi', 1999, 5, 15, '256 Adyar', 878237288)

book1 = Book('Divine Dinosaurs', 200, 2020, 4, 29, author1)
book2 = Book('Rocket Science', 200, 2021, 4, 29, author1)
book3 = Book('How to overcome laziness', 500, 2010, 4, 29, author2)

books = [book1, book2, book3]
for book in books:
    book.display()
print()

print('List of books sorted by publishing date')
for book in sorted(books):
    print(book.title)
print()

print('List of books by young authors')
for book in books:
    if book.author.age < 18:
        print(book.title)
print()

print(f'Author details of "{book1.title}"')
book1.author_details()
