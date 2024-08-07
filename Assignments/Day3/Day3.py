class Client:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
class Bank:
    def __init__(self , account_number , holder_name , balance):
        global balances
        balances = { }
        balances[account_number] = Client(account_number , holder_name , balance)
    def deposit(self , account_number ,amount):
        balances[account_number].balance+=amount
    def withdraw(self , account_number , amount):
        if amount > balances[account_number].balance:
            print("Amount cant be greater than the user balance")
            return
        balances[account_number].balance -=amount
    def display_balance(self , account_number):
        print(balances[account_number].balance)

bank = Bank(1001 , "Anjanay Raina" , 10000000)
bank.display_balance(1001)
bank.deposit(1001 , 100)
bank.display_balance(1001)
bank.withdraw(1001 , 100)
bank.display_balance(1001)
bank.withdraw(1001 , 100000000000)