# Crie uma classe churrasco, onde seja possivel informar quantas pessoas vão participar
# e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
# CONSIDERE:
    # Consumo padrão = 400g por pessoa
    # Preço da carne = R$82,40/Kg

from rich import print
from rich.panel import Panel

class Churrasco:
    # atributos de Classe
    consumo_padrao = 0.4  # kg por pessoa
    preco_carne = 82.4      # preço por kg

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade  # número de pessoas

    def __str__(self):
        return f'O churrasco {self.titulo} tem {self.quantidade} pessoas'
    
    def calcular_qtd_carne(self):
        return self.quantidade * self.consumo_padrao
    
    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * self.preco_carne
    
    def calcular_custo_individual(self):
        return self.calcular_qtd_carne() * self.preco_carne / self.quantidade

    def analisar(self):
        conteudo = f'Analisando o [bold green]{self.titulo}[/] com [bold blue]{self.quantidade} pessoas[/]\n'
        conteudo += f'[bold white]Cada participante comerá {Churrasco.consumo_padrao:.1f}Kg e cada Kg custa R${Churrasco.preco_carne:,.2f}[/]\n'
        conteudo += f'Recomendo [bold blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne\n'
        conteudo += f'O custo total será de [bold green]R${self.calcular_custo_total():,.2f}[/]\n'
        conteudo += f'Cada pessoa pagará [bold yellow]R${self.calcular_custo_individual():,.2f}[/] para participar.'

        imprimir = Panel(conteudo,title=self.titulo)
        print(imprimir)


# Exemplo de uso
# Criando instâncias
c1 = Churrasco('Churras dos Amigos', 10)
c2 = Churrasco('Festa fim de Ano', 80)

# Imprimindo
c1.analisar()
c2.analisar()