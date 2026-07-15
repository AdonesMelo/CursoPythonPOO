class ContaBancaria:
    '''
    Criar uma classe conta bancária, que permite fazer saques e depósitos.
    '''
    def __init__(self, id, nome, saldo=0):
        self.id = id            # (+) Atributo Público
        self._titular =  nome   # (#) Atributo Protegido
        self.__saldo = saldo    # (-) Atributo Privado
        print(f'Conta {self.id} criada com sucesso. Saldo atual: R${self.__saldo:,.2f}.')
    
    def __str__(self):
        #return f'Conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'
        return f'Estado atual da conta: {self.__dict__}'
    
    def depositar(self, valor):
        valor = abs(valor) # Converter para valor absoluto, ex: se receber -500, converter para 500
        self.__saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}.')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'SALDO INSUFICIENTE: Saque NEGADO para R${valor:,.2f} na conta {self.id}.')
        else:
            self.__saldo -= valor
            print(f'Saco de R${valor:,.2f} autorizado na conta {self.id}.')