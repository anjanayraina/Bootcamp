
from exceptions import InvalidAccountNumberError

def validate_account_number(account_number):
    if not isinstance(account_number, str) or len(account_number) != 10 or not account_number.isdigit():
        raise InvalidAccountNumberError("Invalid account number. It must be a 10-digit number.")
    return True
