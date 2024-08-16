from Transaction import Transaction
class WithdrawalTransaction(Transaction):
    def __init__(self, account, amount, location):
        super().__init__(amount, location)
        self.account = account

    def process(self):
        self.account.withdraw(self.amount)
