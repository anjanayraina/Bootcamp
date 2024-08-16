from BankAccount import BankAccount

class SecureBankAccount(BankAccount):
    def __init__(self, account_number, balance=0, password=None, transaction_limit=10000):
        super().__init__(account_number, balance)
        self.password = password
        self.transaction_limit = transaction_limit

    def deposit(self, amount):
        if self._security_check():
            self._balance += amount
        else:
            raise PermissionError("Security check failed")

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            raise ValueError("Transaction exceeds limit")
        if self._security_check() and self._balance >= amount:
            self._balance -= amount
        else:
            raise PermissionError("Security check failed or insufficient funds")

    def transfer(self, amount, target_account):
        if amount > self.transaction_limit:
            raise ValueError("Transaction exceeds limit")
        if self._security_check() and self._balance >= amount:
            self._balance -= amount
            target_account.deposit(amount)
        else:
            raise PermissionError("Security check failed or insufficient funds")

    def _security_check(self):
        input_password = input(f"Enter password for account {self._account_number}: ")
        return input_password == self.password
