
from exceptions import InsufficientFundsError


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this transaction.")
        self.balance -= amount
        return self.balance
