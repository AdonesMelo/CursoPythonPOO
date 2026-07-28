from abc import ABC, abstractmethod
from datetime import date 

class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self._nascimento = None

        # Validação
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano: int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f'Ano {ano} invalido.')

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self):
        raise PermissionError('Voce não pode alterar a idade. Mude o ano de nascimento.')
    
    
class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome: str, nascimento: int, curso: str):
        super().__init__(nome, nascimento)
        self._curso = None

        # Validação
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f'Curso {curso} inválido. Não está na lista de cursos oficiais.')

    def add_curso(self, curso):
        curso = curso.strip().upper()

        if curso in Aluno.cursos_oficiais:
            raise ValueError(f'Curso {curso} já existe.')
        elif 3 <= len(curso) <= 5:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f'Nome {curso} fora do padrão para curso.')