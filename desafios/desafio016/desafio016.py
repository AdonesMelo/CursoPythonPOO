# Crie a classe fucionario, onde podemos cadastrar nome, setor e cargo.
# Crie tambem um metodo que permite o fucionario se apresentar
from rich import print
from rich import inspect

class Fucionario:
    # Atributo de classe
    empresa='Curso em Video'

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome 
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Fucionario.empresa}.'


f1 = Fucionario('Maria', 'Administração', 'Diretora')
print(f1.apresentacao())
#inspect(f1) # Inspectar instância

f2 = Fucionario('Pedro', 'TI', 'Programador')
print(f2.apresentacao())
#inspect(f2) # Inspectar instância

#inspect(Fucionario) # Inspectar classe