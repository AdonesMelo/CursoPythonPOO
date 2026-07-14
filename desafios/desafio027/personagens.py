from abc import ABC, abstractmethod
from rich import print
import random

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
        
    def atacar(self, alvo, forca=10):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com [yellow]{golpe}[/] de força [blue]{forca}[/]!')

            alvo.receber_dano(forca)
            
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer!')
    
    def receber_dano(self, dano):
        fator = random.randint(1, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]!')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe de Machado', 'Pulo Giratório', 'Golpe de Espada', 'Golpe Voador']

    def curar(self):
        fator = random.randint(1, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida!')


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio de Luz', 'Magia das Sombras', 'Magia Estatica', 'Magia Elemental']

    def curar(self):
        fator = random.randint(1, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] fez uma magia e [green]recuperou {fator} pontos[/] de vida!')