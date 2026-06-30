# Declaração de uma classe
class Gafanhoto:
    '''
    Essa classe cria um Gafanhoto, que é uma pessoa que tem um nome e idade.
    O atributo nome é opcional, caso não seja informado, o valor padrão é 'Vazio'.
    O atributo idade é opcional, caso não seja informado, o valor padrão é 0.

    Para criar uma nova pessoa, use
        variável = Gafanhoto('Nome', idade)
    '''
    def __init__(self, nome='Vazio', idade=0): # Método de Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade
    
    # Métodos de Instância
    def aniversario(self):
        self.idade  = self.idade + 1
    
    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'
    
    def __getstate__(self): # Dunder Method
        return f'Estado: nome = {self.nome}; idade ={self.idade}'

# Declaração de objetos
g1 = Gafanhoto('Maria', 17)
g1.aniversario()
print(g1)
print(g1.__dict__) # Mostra os atributos da classe
print(g1.__getstate__()) # Mostra o estado da classe
print(g1.__class__) # Mostra a classe da classe
print(g1.__doc__) # Mostra a documentação da classe