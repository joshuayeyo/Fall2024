# page 384 은행계좌
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance = amount
        print("통장에서", amount, "출금되었음")

    def deposit(self, amount):
        self.balance = amount
        print("통장에", amount, "입금되었음")

a = BankAccount()
a.deposit(10)
a.withdraw(100)
