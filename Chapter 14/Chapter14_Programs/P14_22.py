class BankAccount:
    account_holders = []

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        BankAccount.account_holders.append(self.owner_name)


account1 = BankAccount('7348', 'Tom', 50)
account2 = BankAccount('6378', 'Bob', 400)
account3 = BankAccount('8348', 'Ron', 500)

print(BankAccount.account_holders)


