import random
class User:
    def __init__(self, username, email_address):    
        self.name = username			
        self.email = email_address		
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):	
        self.account.deposit(amount)
        #print(self.account.display_account_info())
        return self

    def make_whitdrawal(self, amount):
        self.account.whitdraw(amount)
        #print(self.account.display_account_info())
        return self

    def display_user_balance(self):
        print(f"Nombre: {self.name}" )
        self.account.display_account_info()
        return self

    def transfer_money(self,other_user,amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        #self.number = random.randint(1000,2000)
    
    def deposit(self, amount):
        self.balance += amount
        
        
    def whitdraw(self, amount):
        if (self.balance < 5):
            print(f"Fondos insuficientes")
        else:
            self.balance -= amount
        
    
    def display_account_info(self):
        #print(f"Numero de cuenta: {self.number}")
        print(f"Saldo: {self.balance}")
        
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate 
        

juan = User("Juan", "juan@empresa.cl")
pedro = User("Pedro", "pedro@empresa.cl")

juan.make_deposit(100)
juan.make_whitdrawal(50).display_user_balance().make_deposit(50).account.yield_interest()
juan.display_user_balance().transfer_money(pedro, 50).display_user_balance()
pedro.display_user_balance()