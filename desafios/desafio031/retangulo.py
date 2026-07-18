class Retangulo:

    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None
        # Atribuindo valores iniciais
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise ValueError('Valor deve ser um número')
        elif valor < 0:
            raise ValueError('Valor inválido para base')
        else:
            self._base = valor
        
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, int) and not isinstance(valor, float):
            raise ValueError('Valor deve ser um número')
        elif valor < 0:
            raise ValueError('Valor inválido')
        else:
            self._altura = valor

    @property
    def medidas(self):
        return f'Base: {self.base} \nAltura: {self.altura} \nArea: {self.area} m²'
    
    @medidas.setter
    def medidas(self, valores: tuple):
        if not isinstance(valores, tuple):
            raise TypeError('Valores deve ser um tupla')
             
        if len(valores) != 2:
            raise ValueError('Informe uma tupla com 2 valores')
        elif isinstance(valores[0], int) or isinstance(valores[0], float):
            self.base = valores[0]
        else:
            raise TypeError('Base deve ser um número')
        
        if isinstance(valores[1], int) or isinstance(valores[1], float):
            self.altura = valores[1]
        else:
            raise TypeError('Altura deve ser um número')

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError('Area não pode ser configurada dessa forma')