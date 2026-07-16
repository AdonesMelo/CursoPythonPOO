from ex010 import Avaliacao
from rich import print, inspect

def main():
    a1 = Avaliacao('Gabriel', 'Inglês')
    a1.nota = 3.5
    print(f'[blue]{a1.nome}[/] tirou [green]{a1.nota}[/] em [yellow]{a1.diciplina}[/].')
    inspect(a1, private=True)
    

if __name__ == '__main__':
    main()