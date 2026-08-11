class Numero:
    def __init__(self, valor: int|float=0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f'Tenho o valor {self.valor} dentro do Número'

class Texto:
    def __init__(self, txt: str=''):
        self.txt = txt

    def dobrar(self):
        self.txt = self.txt + ' ' + self.txt

    def __str__(self):
        return f'Tenho o texto "{self.txt}" dentro do Texto'


class Lista:
    def __init__(self, lista: list=[]):
        self.valores = lista

    def dobrar(self):
        self.valores = self.valores  + self.valores

    def __str__(self):
        return f'Tenho os itens {self.valores} dentro da Lista'

class Papel:
    def __init__(self):
        self.drobado = False

    def dobrar(self):
        self.drobado = True

    def __str__(self):
        return f'O papel está {"Novo" if not self.drobado else "Drobado"}'


class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f'Era uma casa muito engraçada...'


# METODO PYTHOTONICO POLIMORFICO DUCK TYPING
def dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f'Tive dificuldade para dobrar o objeto {objeto.__class__.__name__}')