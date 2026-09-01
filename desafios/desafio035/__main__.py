
from classes_035 import *

def main():
    a1 = PDF('Prova', 450_000)
    a2 = DOC('Contato', 100_000)

    abrir_arquivo(a1)
    abrir_arquivo(a2)


if __name__ == '__main__':
    main()