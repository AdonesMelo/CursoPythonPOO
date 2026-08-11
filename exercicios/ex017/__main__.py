from classes import *

def main():
    a = Numero(200)
    b = Texto('Python')
    c = Lista([1, 2, 3])
    d = Papel()
    e = Casa()

    dobrar(a)
    dobrar(b)
    dobrar(c)
    dobrar(d)
    dobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

if __name__ == '__main__':
    main()