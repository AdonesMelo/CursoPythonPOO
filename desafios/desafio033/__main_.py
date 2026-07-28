from pessoa import *
from rich import print, inspect

def main():
    a1 = Aluno('João', 1990, 'ADM')
    a2 = Aluno('Maria', 1990, 'ADS')
    a1.add_curso('moda')
    a2.add_curso('dir')

    print(a2.cursos_oficiais)
    inspect(a2, methods=True, private=True)



if __name__ == '__main__':
    main()