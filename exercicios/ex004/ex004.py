from rich import print,inspect

class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        print(f'O aluno {self.nome}, matriculou-se no curso {self.curso} na turma {self.turma}.')

        
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):
        print(f'O prof. {self.nome} começou a dar aula!')

        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor  = setor

    def bater_ponto(self):
        print(f'O funcionário {self.nome} bateu ponto!')


a1 = Aluno('José', 17, 'Informática', 'T01')
#print(a1.__dict__)
a1.fazer_matricula()
a1.fazer_aniversario()
#inspect(a1, methods=True)

p1 = Professor('Guanabarra', 42, 'TI', 'Mestrato')
p1.dar_aula()
p1.fazer_aniversario()
#inspect(p1, methods=True)

f1 = Funcionario('Maria', 25, 'Secretária', 'Secretaria')
f1.bater_ponto()
f1.fazer_aniversario()
inspect(f1, methods=True)
