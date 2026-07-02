# Crie uma classe gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie tambem um metodo que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = [] # pode usar list() ou []

    def add_favorito(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Nome Real: [blue on black]{self.nome}[/]\n'
        conteudo += f'Jogos Favoritos:\n'
        for game in self.favoritos:
            conteudo += f':video_game: [blue]{game}[/]\n'
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', style='white', width=34)
        print(painel)


g1 = Gamer('Adones Melo', 'Doni88')
g1.add_favorito('Mario Bros')
g1.add_favorito('CS:GO')
g1.add_favorito('Fifa')
g1.add_favorito('Fortnite')
#inspect(g1)
g1.ficha()

g2 = Gamer('Maria Eduarda', 'Duda26')
g2.add_favorito('Mario Bros')
g2.add_favorito('Minicraft')
g2.add_favorito('Donkey Kong')
g2.add_favorito('BOMBERMAN')
#inspect(g2)
g2.ficha()