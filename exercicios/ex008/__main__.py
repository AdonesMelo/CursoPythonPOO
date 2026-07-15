from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(111, 'Maria', 5_000)
    c1.depositar(1_000)
    c1._titular = 'João' # O python deixa, mas não mexa pois 'Adultos estão consentindo'...

    #c1.__saldo = 0 # Aqui ele não conseguiu alterar, ele cria uma nova variável
    c1._ContaBancaria__saldo = 0 # Não mexa, pois é um atributo privado. Já aqui ele conseguiu alterar!
    print(c1)

if __name__ == '__main__':
    main()