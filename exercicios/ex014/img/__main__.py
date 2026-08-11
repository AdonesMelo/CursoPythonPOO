from analisador import *

def main():
    a1 = Analisador()
    a1.analisar(38)
    a1.analisar(3.14)
    a1.analisar('Python')
    a1.analisar([1, 2, 3])
    a1.analisar({'nome': 'João', 'idade': 30})
    a1.analisar(('POO', 'Python'))

if __name__ == '__main__':
    main()