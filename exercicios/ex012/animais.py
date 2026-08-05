# Polimorfismo

from abc import ABC, abstractmethod

class Animal:
    def __init__(self, nome=''):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e está emitindo som')



class Pato(Animal):
    def emitir_som(self):
            print(f'{self.nome} acabou de fazer "QUACK! QUACK!"')


class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de fazer "MIAU! MIAU!"')


class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de fazer "AU! AU! AU!"')


class Pitbull(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} acabou de fazer "RUFF! RUFF! RUFF!"')


class Spitz(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} acabou de fazer "au! au! au! au! au! au! au! au!"')


class Galinha(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de fazer "PO! PO! PO!"')