class Avaliacao:

    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota # Atributo protegido

    # Metodos Accessores
    def get_nota(self): # Método getter
        return self._nota

    def set_nota(self, valor): # Método setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')