
class Account():
    rate = 5

    def __init__(self):
        self.rate = 10

    def display(self):
        print(Account.rate, self.rate)

a = Account()
a.display()

