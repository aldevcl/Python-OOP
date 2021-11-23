class User:
    def __init__(self, username, email_address):    
        self.name = username			
        self.email = email_address		
        self.account_balance = 0	

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_whitdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

juan = User("Juan Perez", "juan@hola.com")
pedro = User("Pedro Soto", "pedro@hola.cl")
ana = User("Ana Solis", "ana@hola.cl")

juan.make_deposit(100).make_deposit(200).make_deposit(300).make_whitdrawal(50).display_user_balance()

pedro.make_deposit(200).make_deposit(500).make_whitdrawal(50).make_whitdrawal(40).display_user_balance()

ana.make_deposit(1000).make_whitdrawal(30).make_whitdrawal(40).make_whitdrawal(70).display_user_balance()

print("-----TRANSFERENCIA-----")

juan.transfer_money(pedro,100)
juan.display_user_balance()
pedro.display_user_balance()