# Crie uma classe caneta, que simule  o funcionameto de uma caneta colorida,
# podendo escrever frases na cor relativa

from rich import print

class Caneta:
    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().strip():
            case 'verde':
                escolha = '[green]'
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case _:
                escolha = 'white'
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f':prohibited: A {self.cor} caneta[/] está tampada')
        else:
            print(f'{self.cor}{msg}[/]', end='')

    def quebrar_linha(self, qtd=1):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


# Teste
c1 = Caneta('vermelho')
c2 = Caneta('verde')
c3 = Caneta('azul')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá mundo!')
c2.escrever('Deu certo!')
c2.quebrar_linha(2)
c3.escrever('Vamos escrever!')
c3.quebrar_linha(5)

c1.tampar()
c1.escrever('Será que rola?')