from bebida_quente import *

def main():
    # Cria objetos de classes BebidaQuente
    b1 = cafe()
    b2 = cha()
    b3 = leite()

    # Chama a classe BebidaQuente
    b1.preparar()
    b2.preparar()
    b3.preparar()


if __name__ == '__main__':
    main()