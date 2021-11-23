class User:
    def __init__(self, username, email_address):    # ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro

    # agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
    	self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)

print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python
print(guido.account_balance)	# salida: 300
print(monty.account_balance)	# salida: 50


