from rich import print,inspect
from classes_ex007 import Aluno, Professor, Funcionario

def main():
    a1 = Aluno('José', 17, 'Informática', 'T01')
    #print(a1.__dict__)
    a1.fazer_matricula()
    a1.fazer_aniversario()
    #inspect(a1, methods=True)

    p1 = Professor('Guanabara', 48, 'TI', 'Mestrato')
    p1.dar_aula()
    p1.fazer_aniversario()
    #inspect(p1, methods=True)

    f1 = Funcionario('Maria', 25, 'Secretária', 'Secretaria')
    f1.bater_ponto()
    f1.fazer_aniversario()
    #inspect(f1, methods=True)

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == '__main__':
    main()
