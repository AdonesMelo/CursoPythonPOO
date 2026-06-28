# Declaração de uma classe
class Gafanhoto:
    def __init__(self): # Método de Construtor
        # Atributos de Instância
        self.nome = ''
        self.idade = 0
    
    # Métodos de Instância
    def aniversario(self):
        self.idade  = self.idade + 1
    
    def mensagem(self):
        print(f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.')

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())
    
g2 = Gafanhoto()
g2.nome = 'João'
g2.idade = 18
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
g3.mensagem()