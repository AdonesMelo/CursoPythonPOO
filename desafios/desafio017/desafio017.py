# Crie a classe produto, onde podemos cadastrar nome, preco.
# Crie tambem um metodo que mosta uma etiqueta de preço do produto.

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} custa R${self.preco:,.2f}'

    def etiqueta(self):
        conteudo = f'[bold white]{self.nome.center(30, " ")}[/]'
        conteudo += f'[bold white]{"-" * 30}[/]'
        precof = f'R${self.preco:,.2f}'
        conteudo += f'[bold white]{precof.center(30, ".")}[/]'

        imprimir = Panel(conteudo, title='Produto', style='white', width=34)
        print(imprimir)

# Criando instâncias
p1 = Produto('Iphone 17 Pro Max', 25_000.85 )
p2 = Produto('Notbook Gamer', 8_000)

# Imprimindo
p1.etiqueta()
p2.etiqueta()