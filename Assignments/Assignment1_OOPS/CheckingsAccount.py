from BankAccount import BankAccount
class CheckingAccount(BankAccount):
    OVERDRAFT_FEE = 35

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance - amount < 0:
                self._balance -= (amount + self.OVERDRAFT_FEE)
            else:
                self._balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive")

    def transfer(self, amount, target_account):
        if amount > 0:
            if self._balance - amount < 0:
                self._balance -= (amount + self.OVERDRAFT_FEE)
            else:
                self._balance -= amount
            target_account.deposit(amount)
        else:
            raise ValueError("Transfer amount must be positive")
