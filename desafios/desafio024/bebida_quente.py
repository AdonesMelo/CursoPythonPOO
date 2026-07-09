from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print('--- Iniciando o Preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- Bebida Pronta ---\n')

    def ferver_agua(self):
        print('1. Ferver a água a 100 graus Celsius.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
        pass

    def misturar(self):
        print('2. Pasando agua pressurizada pelo pó de café moido.')

    def servir(self):
        print('3. Servindo em xícara pequena.')
    

class cha(BebidaQuente):
    def __init__(self):
        super().__init__()
        pass

    def misturar(self):
        print('2. Mergulhando o sachê de ervas na água.')

    def servir(self):
        print('3. Servido na caneca de porcelana com limão.')
    
class leite(BebidaQuente):
    def __init__(self):
        super().__init__()
        pass

    def misturar(self):
        print('2. Passando o vapor pressurizado pelo bico de leite.')

    def servir(self):
        print('3. Servindo na caneca grande, já com café.')