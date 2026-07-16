from ex009 import Avaliacao
from rich import print, inspect

def main():
    a1 = Avaliacao('Gabriel', 'Ingles')
    a1.set_nota(8.5)
    print(f'[blue]{a1.nome}[/] tirou [green]{a1.get_nota()}[/] em [yellow]{a1.diciplina}[/].')
    #inspect(a1, private=True)
    

if __name__ == '__main__':
    main()