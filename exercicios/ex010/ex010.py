class Avaliacao:

    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota

    # Criando atributos validavel
    @property
    def nota(self): # Método getter
        return self._nota

    @nota.setter
    def nota(self, valor): # Método setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')