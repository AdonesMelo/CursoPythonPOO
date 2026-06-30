from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')
tabela.add_column('Nome', justify='center', style='green')
tabela.add_column('Preço', justify='center', style='red')
tabela.add_row('Café', 'R$10,00')
tabela.add_row('Pizza', 'R$12,00')


print(tabela)