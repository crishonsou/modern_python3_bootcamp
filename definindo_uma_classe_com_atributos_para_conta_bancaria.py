class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = 0
    def owner(self):
        return f'Hi {self.name}.'
    def getBalance(self):
        return f'Your balance is ${self.balance:.2f}'
    def deposit(self, amount):
        self.balance += amount
        return f'You made a deposit of: ${amount:.2f}'
    def withdraw(self, amount):
        self.balance -= amount
        return f'You made a withdraw of: ${amount:.2f}'
    
    
acct = BankAccount('Darcy')
print(acct.owner())
print(acct.getBalance())
print(acct.deposit(30.0))
print(acct.withdraw(9.0))
print(acct.getBalance())





    
