from retangulo import *
from rich import print, inspect

def main():
    r = Retangulo()

    try:
        r.base = 12
        r.altura = 7
        r.medidas = (3, 9)
    except Exception as e:
        print(f'[red]ocorreu um erro do tipo {type(e).__name__}: {e}[/]')

    print(r.medidas)
    

if __name__ == '__main__':
    main()