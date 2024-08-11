class FraudDetector:
    def __init__(self):
        self.known_locations = {}

    def analyze(self, transaction, account):
        if transaction.amount > 10000:
            return True

        if account.get_account_number() not in self.known_locations:
            self.known_locations[account.get_account_number()] = set()

        if transaction.location not in self.known_locations[account.get_account_number()]:
            self.known_locations[account.get_account_number()].add(transaction.location)
            return True

        return False
