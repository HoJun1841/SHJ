class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다.')
    
    def tranfer(self, amount, target_account):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다.')


account1 = BankAccount(12345, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000) #출력 : 잔액이 부족합니다.