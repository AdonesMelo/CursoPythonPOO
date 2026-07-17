from diario import *
from rich import print, inspect

def main():
    meu_diario = Diario()
    meu_diario.escrever('Olá mundo!')
    meu_diario.escrever('Python é uma linguagem de programação de alto nível')

    #inspect(meu_diario, methods=True, private=True)

    try:
        # Alterando senha usando o setter 
        meu_diario.senha = ('Admin', 'Admin2')
        meu_diario.ler('Admin2')
    
    except PermissionError as e:
        print(f'[red]ERRO: {e}[/]')
    

if __name__ == '__main__':
    main()