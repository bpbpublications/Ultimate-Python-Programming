class BankAccount:
    rate = 5
    min_balance = 100
    min_balance_fees = 10

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    @classmethod
    def details(cls):
        print(f'Rate : {cls.rate}')
        print(f'Minimum Balance : {cls.min_balance}')
        print(f'Minimum Balance fees : {cls.min_balance_fees}')


BankAccount.details()
