from personagens import *
from rich import inspect

def main():
    p1 = Guerreiro('MegaMan', 1000)
    p2 = Mago('Gandalf', 2000)

    p1.atacar(p2, 200)
    p2.atacar(p1, 200)

    p1.curar()
    p2.curar()
    
    # inspect(p1, methods=True)

if __name__ == '__main__':
    main()