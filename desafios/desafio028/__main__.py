from termostato import *
from rich import print, inspect

def main():
    t = Termostato()
    valor = float(input('Digite a temperatura desejada: '))

    try:
        t.temperatura = valor
    except ValueError as e:
        print(f'Houve um problema: {e}')

    #inspect(t)

    print(f'A temperatura atual é {t.ftemperatura}')


if __name__ == '__main__':
    main()