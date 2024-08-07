class Bank:
    def __init__(self , account_number , holder_name , balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self , amount):
        self.balance+=amount
    def withdraw(self , amount):
        if amount > self.balance  :
            return
        self.balance -=amount
    def display_balance(self ):
        print(self.balance)