from account_validation import validate_account_number
from bank_account import BankAccount
from exceptions import InvalidAccountNumberError, InsufficientFundsError


def main():

    try:
        account_number = "1234567890"
        validate_account_number(account_number)
        print("Test 1 Passed: Account number is valid.")
    except InvalidAccountNumberError as e:
        print(f"Test 1 Failed: {e}")

    try:
        account_number = "12345678"
        validate_account_number(account_number)
        print("Test 2 Failed: Invalid account number was accepted.")
    except InvalidAccountNumberError as e:
        print(f"Test 2 Passed: {e}")

    try:
        account_number = "12345ABCDE"
        validate_account_number(account_number)
        print("Test 3 Failed: Invalid account number was accepted.")
    except InvalidAccountNumberError as e:
        print(f"Test 3 Passed: {e}")

    try:
        account = BankAccount("1234567890", 500)
        new_balance = account.withdraw(200)
        print(f"Test 4 Passed: Withdrawal successful. New balance is: {new_balance}")
    except InsufficientFundsError as e:
        print(f"Test 4 Failed: {e}")

    try:
        account = BankAccount("1234567890", 300)
        account.withdraw(500)
        print("Test 5 Failed: Withdrawal was allowed with insufficient funds.")
    except InsufficientFundsError as e:
        print(f"Test 5 Passed: {e}")

    try:
        account = BankAccount("1234567890", 300)
        new_balance = account.withdraw(300)
        print(f"Test 6 Passed: Withdrawal successful. New balance is: {new_balance}")
    except InsufficientFundsError as e:
        print(f"Test 6 Failed: {e}")


if __name__ == "__main__":
    main()
