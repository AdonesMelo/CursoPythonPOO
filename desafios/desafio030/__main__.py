from crendecial import *
from rich import print, inspect

def main():
    c = Crendecial()
    c.senha = str(input('Digite a senha: '))
    print(f'Hash: {c.senha}')

    c.validar('Admin')

    #inspect(c)

if __name__ == '__main__':
    main()