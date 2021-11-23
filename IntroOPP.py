class User:		# declara una clase y dale el nombre User
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

guido = User()
monty = User()

print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael

guido.name="Guido"
monty.name="Monty"

print(guido.name)	# salida: Guido
print(monty.name)	# salida: Monty
