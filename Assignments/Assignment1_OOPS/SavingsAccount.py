from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    MINIMUM_BALANCE = 1000

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= self.MINIMUM_BALANCE:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds or minimum balance requirement not met")

    def transfer(self, amount, target_account):
        if amount > 0 and (self._balance - amount) >= self.MINIMUM_BALANCE:
            self._balance -= amount
            target_account.deposit(amount)
        else:
            raise ValueError("Insufficient funds or minimum balance requirement not met")

