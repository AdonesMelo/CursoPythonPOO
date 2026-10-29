import sqlite3
from datetime import date

busca = input('Quem você está procurando: ').strip()
hoje = date.today()

try:
    with sqlite3.connect('meubanco.db') as banco:
        banco.row_factory = sqlite3.Row # Pegar os nomes das colunas
        cur = banco.cursor()
        cur.execute('SELECT * FROM amigos WHERE nome LIKE ?', (f'%{busca}%',))

        total = 0

        for total, amigo in enumerate(cur, start=1):
            txt_nasc = amigo['nascimento']

            info_nasc = ''
            if not txt_nasc:
                info_nasc = 'sem data de nascimento'
            else:
                try:
                    data = date.fromisoformat(str(txt_nasc))

                    # Verifica se a data de nascimento já passou neste ano
                    ja_passou = (hoje.month, hoje.day) >= (data.month, data.day)
                    idade = hoje.year - data.year - (0 if ja_passou else 1)

                    info_nasc = f'nasceu em {data:%d/%m/%Y} e tem {idade} anos'

                except ValueError:
                    info_nasc = 'data de nascimento inválida'

            print(f'{amigo["nome"]} {info_nasc}')

        print('-' * 30)

        if total == 0:
            print(f'Não encontrei ninguém com {busca} no nome.')
        elif total == 1:
            print(f'Encontrei apenas um amigo com {busca}.')
        else:
            print(f'Ao todo encontrei {total} amigos com "{busca}".')

except sqlite3.Error as erro:
    print(f'Erro na conexão com o banco de dados: {erro}')
except Exception as erro:
    print(f'Algo deu errado: {erro}')