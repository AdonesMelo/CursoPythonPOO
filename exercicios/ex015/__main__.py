from carteira import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(160)
    print(c1 == c2)

    c1 += 100
    c1 -= 50

    if c1 == c2:
        print('Carteiras são iguais')
    else:
        print('Carteiras não são iguais')


    print(c1)
    print(c2)

if __name__ == '__main__':
    main()