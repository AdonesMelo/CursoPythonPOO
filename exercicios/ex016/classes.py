class Porta:
    def abrir(self):
        print('Gira a maçaneta e empurrar/puxar a porta')


class Empresa:
    def abrir(self):
        print('Vai até o portal do emprendor com todas documentações para abrir o CNPJ')


class Ovo:
    def abrir(self):
        print('Quebra a casca com uma colher e sepera as partes sobre a frigideira')


class Pedra:
    pass


#METODO PYTHOTONICO POLIMORFICO DUCK TYPING
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Encontrei um erro ao tentar abrir objeto do tipo {objeto.__class__.__name__}')
        