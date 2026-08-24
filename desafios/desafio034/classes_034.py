from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str = None, salario: float = 1_621):
        self.nome = nome            # Atributo Público
        self.__salario = salario    # Atributo Privado

    @abstractmethod
    def calcular_bonus(self):
        pass

    # getters e setters
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor: float):
        if valor is None:
             raise valeuError('Impossível reajustar o salário desse jeito.')
        elif valor < self.__salario:
            raise ValueError('O salario do funcionário não pode ser reduzido.')
        else:
            self.__salario = valor

    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}.'
    
    
class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15 # 15% de bônus


class Designer(Funcionario):
    def calcular_bonus(self):
            return self.salario * 0.08 # 8% de bônus
            

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
            return self.salario * 0.10 # 10% de bônus