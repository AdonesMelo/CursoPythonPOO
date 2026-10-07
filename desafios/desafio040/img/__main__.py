from classes_040 import *

def main():
    u = [
        Usuario('João', 'joao@gmail.com'),
        Usuario('Maria', 'maria@gmail.com'),
    ]

    a = [
        Aluno('João', 'ADS', 'T01'),
        Aluno('Maria', 'ADM', 'T02'),
        Aluno('Pedro', 'ENG', 'T03'),
        Aluno('Ana', 'CONT', 'T04'),
        Aluno('Luiz', 'MAT', 'T05'),
    ]

    exportar_dados(XML(), u)
    print()
    exportar_dados(JSON(), a)

if __name__ == '__main__':
    main()