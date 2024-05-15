class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.balance}'

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __bool__(self):
        return self.balance != 0


a1 = BankAccount('Mike', 200)
a2 = BankAccount('Tom')

print(a1)
print(a2)

if not a2:
    print('Empty account')
print(bool(a1), bool(a2))
