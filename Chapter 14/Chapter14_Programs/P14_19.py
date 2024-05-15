class BankAccount:
    rate = 5
    min_balance = 1000
    min_balance_fees = 10

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount('7348', 'Tom', 50)
account2 = BankAccount('6378', 'Bob', 400)
