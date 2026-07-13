from rich import print, inspect
from rich.table import Table
from transportes import *

def main():
    while True:
        try:
            distc = float(input('> Distância em km: '))
            viagens = [Moto(distc), Caminhao(distc), Drone(distc)]

            tabela = Table(title='Tabela de Fretes')
            tabela.add_column('Distância')
            tabela.add_column('Tipo')   
            tabela.add_column('Frete')

            for viagem in viagens:
                tabela.add_row(f'{viagem.distancia}km', f'{type(viagem).__name__}', f'{viagem.calc_frete()}')

            print(tabela)

            print('> Deseja calcular outra viagem? (s/n)')
            if input('> ').lower() == 's':
                continue
            else:
                break

        except ValueError:
            print('Valor inválido\n')

    # Outra opção de implementação   
    
    # opcoes = {
    #     1: Moto,
    #     2: Caminhao,
    #     3: Drone
    # }

    # while True:
    #     print('Escolha uma opção:')
    #     print('[1] Moto')
    #     print('[2] Caminhão')
    #     print('[3] Drone')
    #     print('[0] Sair')

    #     opcao = int(input('> '))

    #     if opcao == 0:
    #         print('Adeus!')
    #         break

    #     if opcao in opcoes:
    #         dist = int(input('> Distância em km: '))
    #         entrega = opcoes[opcao](dist)
    #         print(f'Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}')
    #     else:
    #         print('Opção inválida\n')

    
if __name__ == '__main__':
    main()