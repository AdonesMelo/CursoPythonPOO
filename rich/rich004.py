from rich import print
from rich import inspect

class ContaBancaria:
    '''
    Criar uma classe conta bancária, que permite fazer saques e depósitos.
    '''
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular =  nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual: R${self.saldo:,.2f}.')
    
    def __str__(self):
        return f'Conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}.')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'SALDO INSUFICIENTE: Saque NEGADO para R${valor:,.2f} na conta {self.id}.')
        else:
            self.saldo -= valor
            print(f'Saco de R${valor:,.2f} autorizado na conta {self.id}.')


c = ContaBancaria(111, 'João', 5000)
inspect(c)