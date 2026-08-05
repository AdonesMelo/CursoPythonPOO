class Mae:
    def __init__(self, nome='Mainha'):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite condensado e calda!')

    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA no óleo de soja!')


# Polimorfismo de inclusão ou sobrecarga(Override)
class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com Leite Ninho e Nutella!')


# Polimorfismo de inclusão ou sobrecarga(Override)
class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA na Air Frayer!')
    