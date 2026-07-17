from rich import print

class Diario:

    def __init__(self, senha_admin='Admin'):
        self.__segredos = []
        self.__senha = senha_admin.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())
    
    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError('Senha incorreta, não está autorizado a ler o diario!')
        else:
            print('[green]DIARIO LIBERADO![/]')
            for segredo in self.__segredos:
                print(f'- [blue]{segredo}[/]')

    @property
    def senha(self):
        raise PermissionError('Não autorizado')
    
    @senha.setter
    def senha(self, pacote):
        '''
        Setter recebe apenas um argumento (pacote),
        então usamos uma tupla ou dict para passar senha antiga e nova.
        '''
        senha_antiga, nova_senha = pacote
        if self.__senha == senha_antiga.strip():
            self.__senha = nova_senha.strip()
        else:
            raise PermissionError('Senha incorreta, não está autorizado a alterar a senha!') 