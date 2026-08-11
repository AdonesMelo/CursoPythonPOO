
from functools import singledispatchmethod

class Analisador:
    @singledispatchmethod
    def analisar(self, valor):
        print(f'Não foi possível analisar o valor {valor}')

    @analisar.register
    def _(self, valor: int):
        print(f'{valor} é um  inteiro')

    @analisar.register
    def _(self, valor: str):
        print(f'"{valor}" é uma cadeia de caracteres(String)')

    @analisar.register
    def _(self, valor: float):
        print(f'{valor} é um número de ponto flutuante(Real)')

    @analisar.register
    def _(self, valor: list|tuple|dict): 
        print(f'{valor} é uma coleção de dados')