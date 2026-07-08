from poligono import *
from rich import print, inspect

def main():
    q1 = Quadrado(12) # Chama a classe Quadrado ou Circulo

    print('\n[green on black]Quadrado[/]')
    print(f'Perimetro: {q1.perimetro():.1f}cm')
    print(f'Área: {q1.area():.1f}cm²')
    #inspect(q1)

    c1 = Circulo(20)
    print('\n[green on black]Circulo[/]')
    print(f'Perimetro: {c1.perimetro():.1f}cm')
    print(f'Área: {c1.area():.1f}cm²')
    #inspect(c1, methods=True)


if __name__ == '__main__':
    main()