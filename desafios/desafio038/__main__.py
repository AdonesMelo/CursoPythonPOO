from classes_038 import *

def main():
    p1 = Produto('Mouse', 129.99)
    p2 = Produto('Teclado', 235.58)
    p3 = Produto('Monitor', 1549.78)
    p4 = Produto('Fone', 144.83)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p2 + p4
    c2 = c2 + c1 + p3

    print(c1)
    print(c2)

if __name__ == '__main__':
    main()