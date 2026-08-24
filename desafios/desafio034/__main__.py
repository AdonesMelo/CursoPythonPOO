from classes_034 import *
from rich import print

def main():
    # Criar objetos
    funcionarios = [
        Designer('João', 11_000),
        Gerente('Maria', 15_000),
        Desenvolvedor('Pedro', 14_000)
    ]

    # Imprimir objetos
    for funcionario in funcionarios:
        print(funcionario)

if __name__ == '__main__':
    main()