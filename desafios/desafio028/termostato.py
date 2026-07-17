class Termostato:
    temp_min = 16
    temp_max = 30
    temp_inicial = 24

    def __init__(self):
        self.__temperatura = Termostato.temp_inicial

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f'Temperatura de {valor}°C é inválida')
        elif valor < Termostato.temp_min:
            self.__temperatura = Termostato.temp_min
        elif valor > Termostato.temp_max:
            self.__temperatura = Termostato.temp_max
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f'{self.temperatura}°C'
