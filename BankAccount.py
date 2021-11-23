class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def whitdraw(self, amount):
        if (self.balance < 5):
            print("Fondos insuficientes")
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Saldo: {self.balance}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate 
        return self 
    
cuenta1 = BankAccount(0.01, 0)
cuenta2 = BankAccount(0.05, 1000)

cuenta1.deposit(100).deposit(100).deposit(100).whitdraw(100).yield_interest().display_account_info()
cuenta2.deposit(200).deposit(1600).whitdraw(50).whitdraw(20).whitdraw(5).whitdraw(100).yield_interest().display_account_info()