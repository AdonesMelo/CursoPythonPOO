from abc import ABC, abstractmethod
import re

class Validador(ABC):
    @abstractmethod
    def validar(self, valor):
        pass


class Usuario(Validador):
    def validar(self, valor: str) -> bool:
        padrao = r'^[a-z0-9_]{5,20}$'
        if re.fullmatch(padrao, valor):
            return True
        else:
            return False


class Email(Validador):
    def validar(self, valor: str) -> bool:
        # Regex para validar o email
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z0-9]{2,}$'

        # Verificar se bate com o padrão
        if re.fullmatch(padrao, valor):
            return True
        else:
            return False

class Senha(Validador):
    def validar(self, valor: str) -> bool:
        # Regex para validar a senha
        padra =r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&?]).{8,}$'

        # Verificar se bate com o padrão
        if re.fullmatch(padra, valor):
            return True
        else:
            return False


# Função genérica para validar
def validador_dados(validador: Validador, valor):
    resultado = validador.validar(valor)
    print(f'Valor: {valor} é válido? {"SIM" if resultado else "NÃO"}')