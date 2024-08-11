from Transaction import Transaction
class TransferTransaction(Transaction):
    def __init__(self, source_account, target_account, amount, location):
        super().__init__(amount, location)
        self.source_account = source_account
        self.target_account = target_account

    def process(self):
        self.source_account.transfer(self.amount, self.target_account)
