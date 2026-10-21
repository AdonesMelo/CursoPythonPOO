import sqlite3

busca = input('Quem você está procurando: ').strip()

try:
    with sqlite3.connect('meubanco.db') as banco:
        banco.row_factory = sqlite3.Row # Pegar os nomes das colunas
        cur = banco.cursor()
        cur.execute('SELECT * FROM amigos WHERE nome LIKE ?', (f'%{busca}%',))

        total = 0

        for total, amigo in enumerate(cur, start=1):
            print(f'{amigo['nome']} naceu em {amigo['nascimento']}')

        print(f'Ao todo encontrei {total} amigos com "{busca}".')

except sqlite3.Error as erro:
    print(f'Erro na conexão com o banco de dados: {erro}')
except Exception as erro:
    print(f'Algo deu errado: {erro}')