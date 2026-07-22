from hashlib import sha256

class ContaBancaria:
    '''
    Criar uma classe conta bancária, que permite fazer saques e depósitos.
    '''
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id           # (+) Atributo Protegido
        self._titular =  nome   # (#) Atributo Protegido
        self.__saldo = saldo    # (-) Atributo Privado
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()   # (-) Atributo Privado

        print(f'Conta {self._id} criada com sucesso. Saldo atual: R${self.__saldo:,.2f}.')

    def pede_senha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = str(pwinput('Senha: '))

            if len(senha) >=6:
                break
            
        return senha

    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False
    
    def __str__(self):
        return f'Conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo.'
        #return f'Estado atual da conta: {self.__dict__}'
    
    def depositar(self, valor):
        valor = abs(valor) # Converter para valor absoluto, ex: se receber -500, converter para 500
        self.__saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self._id}.')

    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'SALDO INSUFICIENTE: Saque NEGADO para R${valor:,.2f} na conta {self._id}.')
            else:
                self.__saldo -= valor
                print(f'Saco de R${valor:,.2f} autorizado na conta {self._id}.')
        else:
            print('Senha não confere. Saque não autorizado!')

    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, novo_nome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novo_nome) >= 5:
                self._titular = novo_nome
        else:
            print('Senha não confere. Atualização não autorizada!')