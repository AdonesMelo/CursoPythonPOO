from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f'R${self.frete:.2f}'
    

class Caminhao(Transporte):
    fator = 1.20
    dist_minimo = 50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < Caminhao.dist_minimo:
            self.frete = 0
            return f'Raio minimo de {Caminhao.dist_minimo}km'
        else:
            self.frete = self.distancia * Caminhao.fator
            return f'R${self.frete:.2f}'
        
class Drone(Transporte):
    fator = 9.50
    dist_maximo = 10

    def __init__(self, distancia):
        super().__init__(distancia)
    
    def calc_frete(self):
        if self.distancia > Drone.dist_maximo:
            self.frete = 0
            return f'Raio maximo de {Drone.dist_maximo}km'
        else:
            self.frete = self.distancia * Drone.fator
            return f'R${self.frete:.2f}'