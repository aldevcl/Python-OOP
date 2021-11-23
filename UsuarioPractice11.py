class User:
    def __init__(self, username, email_address):    
        self.name = username			
        self.email = email_address		
        self.account_balance = 0		

    def make_deposit(self, amount):	
    	self.account_balance += amount	

    def make_whitdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

juan = User("Juan Perez", "juan@hola.com")
pedro = User("Pedro Soto", "pedro@hola.cl")
ana = User("Ana Solis", "ana@hola.cl")

juan.make_deposit(100)
juan.make_deposit(200)
juan.make_deposit(300)
juan.make_whitdrawal(50)
juan.display_user_balance()

pedro.make_deposit(200)
pedro.make_deposit(500)
pedro.make_whitdrawal(50)
pedro.make_whitdrawal(40)
pedro.display_user_balance()

ana.make_deposit(1000)
ana.make_whitdrawal(30)
ana.make_whitdrawal(40)
ana.make_whitdrawal(70)
ana.display_user_balance()

print("-----TRANSFERENCIA-----")

juan.transfer_money(pedro,100)
juan.display_user_balance()
pedro.display_user_balance()