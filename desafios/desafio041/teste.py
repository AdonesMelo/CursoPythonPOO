from datetime import date

hoje = date.today()

teste = (hoje.month, hoje.day) >= (7, 1) # True se a data atual for maior ou igual a 1 de julho, False caso contrário

print(teste)