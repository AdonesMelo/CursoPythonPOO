from familia import *

def main():
    pessoa_1 = Mae('Maria')
    pessoa_2 = Filha('Ana')
    pessoa_3 = Filho('João')

    pessoa_1.fazer_pudim()
    pessoa_1.fritar_coxinha()

    pessoa_2.fazer_pudim()
    pessoa_2.fritar_coxinha()

    pessoa_3.fazer_pudim()
    pessoa_3.fritar_coxinha()

if __name__ == '__main__':
    main()