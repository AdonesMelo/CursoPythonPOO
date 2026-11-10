from crud import *

def exebir_menu():
    print('=' * 30)
    print('SISTEMA DE CADASTRO')
    print('=' * 30)
    print('1 - Cadastrar pessoa')
    print('2 - Listar pessoas')
    print('3 - Atualizar pessoa')
    print('4 - Excluir pessoa')
    print('5 - Buscar por nome')
    print('0 - Sair')
    print('=' * 30)

def main():
    # cadastro_em_massa()     # [IMPORTANTE] Executa o cadastro em massa apenas uma vez, na primeira execução do programa.
    criar_banco()
    if not criar_banco():
        print('Falha na criação do banco de dados. Encerrando o sistema...')
        raise SystemExit

    while True:
        exebir_menu()
        opcao = input('escolha uma opção: ').strip()
        match opcao:
            case '1': # Cadastrar pessoa
                if not cadastrar_pessoa():
                    print('[ERRO] nao foi possivel cadastrar a pessoa.')

            case '2': # Listar pessoas
                if not listar_pessoas():
                    print('[ERRO] nao foi possivel listar as pessoas.')

            case '3': # Atualizar pessoa
                if not atualizar_pessoa():
                    print('[ERRO] nao foi possivel atualizar a pessoa.')

            case '4': # Excluir pessoa
                if not excluir_pessoa():
                    print('[ERRO] nao foi possivel excluir a pessoa.')
            
            case '5': # Buscar por nome
                if not buscar_por_nome():
                    print('[ERRO] nao foi possivel buscar a pessoa.')

            case '0': # Sair
                print('\nEncerrando o Sistema...')
                break
            case _:
                print('\n[ERRO] Opção inválida! Escolha uma valor entre 0 e 5.')

        input('\nPressione ENTER para continuar...')


if __name__ == "__main__":
    main()