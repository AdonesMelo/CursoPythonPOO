from conta_bancaria import *
from rich import print, inspect

def main():
    print('Criando conta...')
    cc = ContaBancaria(111, 'João da Silva', 10_000)

    print('Realizando deposito...')
    cc.depositar(100)

    print('Realizando saque...')
    cc.sacar(500)

    print('Atualizando nome...')
    cc.nome = 'Joãozinho'

    print(cc)

    inspect(cc, methods=True, private=True)
    
if __name__ == '__main__':
    main()