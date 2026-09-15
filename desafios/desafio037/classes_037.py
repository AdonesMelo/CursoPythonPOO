from rich import print
from rich.panel import Panel

class Mensagem():
    def __init__(self, mensagem='', tipo='aviso', icone=':thought_balloon:'):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        conteudo = f'[bold white]{self._mensagem} [/]'
        titulo = f'{self._icone} {self._tipo.upper()} {self._icone}'
        msg  = Panel(conteudo, title=titulo, style='on black', border_style='bold white', width=45)
        print(msg)


class Alerta(Mensagem):
    def __init__(self, mensagem=''):
        super().__init__(mensagem, tipo='alerta', icone=':warning:')
    
    def mostrar(self):
        conteudo = f'[bold black]{self._mensagem}[/]'
        titulo = f'{self._icone} {self._tipo.upper()} {self._icone}'
        msg  = Panel(conteudo, title=titulo, style='on yellow', border_style='bold black', width=45)
        print(msg)


class Erro(Mensagem):
    def __init__(self, mensagem=''):
        super().__init__(mensagem, tipo='erro', icone=':prohibited:')

    def mostrar(self):
        conteudo = f'[bold yellow]{self._mensagem}'
        titulo = f'{self._icone} {self._tipo.upper()} {self._icone}'
        msg  = Panel(conteudo, title=titulo, style='on red', border_style='bold yellow', width=45)
        print(msg)