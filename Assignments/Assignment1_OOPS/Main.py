from Bank import Bank
from SavingsAccount import SavingsAccount
from CheckingsAccount import CheckingAccount
from DepositTransaction import DepositTransaction
from WithdrawalTransaction import  WithdrawalTransaction
from TransferTransaction import TransferTransaction
from SecureBankAccount import SecureBankAccount
from FraudDetection import FraudDetector


def main():
    bank = Bank()
    savings = SavingsAccount('SA123', 5000)
    checking = CheckingAccount('CA456', 2000)
    secure_account = SecureBankAccount('SA789', 10000)

    bank.add_account(savings)
    bank.add_account(checking)
    bank.add_account(secure_account)

    deposit = DepositTransaction(savings, 1000, "New York")
    withdrawal = WithdrawalTransaction(checking, 500, "Los Angeles")
    transfer = TransferTransaction(savings, checking, 2000, "Chicago")

    bank.process_transaction(deposit)
    bank.process_transaction(withdrawal)
    bank.process_transaction(transfer)

    print(bank.generate_statement('SA123'))
    print(bank.generate_statement('CA456'))

    fraud_detector = FraudDetector()

    large_withdrawal = WithdrawalTransaction(secure_account, 20000, "San Francisco")

    if fraud_detector.analyze(large_withdrawal, secure_account):
        print("Fraud detected in transaction")
    else:
        bank.process_transaction(large_withdrawal)

    print(bank.generate_statement('SA789'))


if __name__ == "__main__":
    main()