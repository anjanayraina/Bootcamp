from Bank import Bank
from SavingsAccount import SavingsAccount
from CheckingsAccount import CheckingAccount
from DepositTransaction import DepositTransaction
from WithdrawalTransaction import  WithdrawalTransaction
from TransferTransaction import TransferTransaction
from SecureBankAccount import SecureBankAccount
from FraudDetection import FraudDetector
from Bank import Bank


def main():
    bank = Bank()

    savings = SavingsAccount('SA123', 5000)
    checking = CheckingAccount('CA456', 2000)
    secure_account = SecureBankAccount('SA789', 10000, password="123", transaction_limit=5000)

    bank.add_account(savings)
    bank.add_account(checking)
    bank.add_account(secure_account)

    print("Test 1: Deposit into SavingsAccount")
    deposit_savings = DepositTransaction(savings, 1500, "New York")
    bank.process_transaction(deposit_savings)
    print(bank.generate_statement('SA123'))

    print("Test 2: Withdraw from SavingsAccount")
    try:
        withdraw_savings = WithdrawalTransaction(savings, 6000, "New York")
        bank.process_transaction(withdraw_savings)
    except ValueError as e:
        print(e)
    print(bank.generate_statement('SA123'))

    print("Test 3: Transfer from SavingsAccount to CheckingAccount")
    transfer_to_checking = TransferTransaction(savings, checking, 2000, "New York")
    bank.process_transaction(transfer_to_checking)
    print(bank.generate_statement('SA123'))
    print(bank.generate_statement('CA456'))

    print("Test 4: Withdraw from CheckingAccount with Overdraft")
    withdraw_checking = WithdrawalTransaction(checking, 4500, "Los Angeles")
    bank.process_transaction(withdraw_checking)
    print(bank.generate_statement('CA456'))

    print("Test 5: Transfer from CheckingAccount to SavingsAccount")
    transfer_to_savings = TransferTransaction(checking, savings, 1000, "Chicago")
    bank.process_transaction(transfer_to_savings)
    print(bank.generate_statement('SA123'))
    print(bank.generate_statement('CA456'))

    print("Test 6: Deposit into SecureBankAccount")
    deposit_secure = DepositTransaction(secure_account, 3000, "San Francisco")
    bank.process_transaction(deposit_secure)
    print(bank.generate_statement('SA789'))

    print("Test 7: Withdraw from SecureBankAccount within limits")
    fraud_detector = FraudDetector()
    small_withdrawal = WithdrawalTransaction(secure_account, 3000, "San Francisco")
    if not fraud_detector.analyze(small_withdrawal, secure_account):
        bank.process_transaction(small_withdrawal)
    print(bank.generate_statement('SA789'))

    print("Test 8: Attempt to withdraw from SecureBankAccount exceeding limit")
    try:
        large_withdrawal = WithdrawalTransaction(secure_account, 6000, "San Francisco")
        if not fraud_detector.analyze(large_withdrawal, secure_account):
            bank.process_transaction(large_withdrawal)
    except ValueError as e:
        print(e)
    print(bank.generate_statement('SA789'))


if __name__ == "__main__":
    main()