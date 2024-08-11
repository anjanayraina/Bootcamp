class Bank:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def add_account(self, account):
        self.accounts[account.get_account_number()] = account

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            raise ValueError("Account not found")

    def process_transaction(self, transaction):
        transaction.process()
        self.transactions.append(transaction)

    def generate_statement(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return f"Account {account.get_account_number()} - Balance: {account.get_balance()}"
        else:
            raise ValueError("Account not found")
