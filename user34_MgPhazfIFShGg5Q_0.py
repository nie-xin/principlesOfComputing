class BankAccount:
    def __init__(self, initial_balance):
        # Creates an account with the given balance.
        self.balance = initial_balance
        self.fees = 0
        
    def deposit(self, amount):
        # Deposits the amount into the account.
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        # Withdraws the amount from the account.  Each withdrawal resulting in a
        # negative balance also deducts a penalty fee of 5 dollars from the balance.
        self.balance = self.balance - amount
        if self.balance < 0:
            self.balance = self.balance - 5
            self.fees = self.fees + 5
            
    def get_balance(self):

        return self.balance
        
    def get_fees(self):
        # Returns the total fees ever deducted from the account.
        return self.fees
    
 
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()