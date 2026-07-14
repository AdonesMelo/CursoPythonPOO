from funcionarios import *
from rich import inspect

def main():
    f1 = FucionarioHorista('João Pedro', 45)
    f1.calc_sal()
    f1.analisar_sal()
    #inspect(f1)

    f2 = FucionarioMensalista('Maria Eduarda', 8500) 
    f2.calc_sal()
    f2.analisar_sal()
    
if __name__ == '__main__':
    main()