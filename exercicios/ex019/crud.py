import sqlite3

NOME_BANCO = r'exercicios\ex019\cadastro.db'

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS pessoas (
                    cod INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    altura REAL NOT NULL
                )
            ''')

        return True

    except sqlite3.Error as erro:
        print(f'Falha na criação do banco de dados: {erro}')
        return False

def cadastro_em_massa():
    cad_pessoas = [
        ('1', 'João', 1.75),
        ('2', 'Maria', 1.65),
        ('3', 'Pedro', 1.80),
        ('4', 'Ana', 1.70),
        ('5', 'Lucas', 1.85),
        ('6', 'Carla', 1.60),
        ('7', 'Rafael', 1.90),
        ('8', 'Juliana', 1.68),
        ('9', 'Gustavo', 1.78),
        ('10', 'Fernanda', 1.72)
    ]

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.executemany('INSERT INTO pessoas (cod, nome, altura) VALUES (?, ?, ?)', cad_pessoas)

    except sqlite3.Error as erro:
        print(f'Falha no cadastro em massa: {erro}')

def cadastrar_pessoa() -> bool:
    print('\n=== NOVO CADASTRO DE PESSOA ===')

    # Leitura e validação dos dados do usuário
    val_nome = input('Nome: ').strip()
    if not val_nome:
        print('[ERRO] O nome é uma campo obrigatório!')
        return False
    
    val_altura = input('Altura: ').strip().replace(',', '.')
    if not val_altura:
        print('[ERRO] A altura é uma campo obrigatório!')
        return False
    try:
        altura = float(val_altura)
        if altura < 0.3 or altura > 3.0:
            print('[ERRO] Valor incoerente para altura!')
            return False
    except ValueError:
        print('[ERRO] A altura deve ser um número válido!')
        return False

    # Inserção dos dados no banco de dados
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute('INSERT INTO pessoas (nome, altura) VALUES (?, ?)', (val_nome, altura))
            print(f'\n[SUCESSO] Pessoa "{val_nome}" cadastrada com sucesso!')
            return True
    except sqlite3.Error as erro:
        print(f'Falha ao cadastrar pessoa: {erro}')
        return False

def listar_pessoas() -> bool:
    print('\n======= LISTA DE PESSOAS CADASTRADAS =======')
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute('SELECT cod, nome, altura FROM pessoas ORDER BY nome;')
            primeiros_registros = cur.fetchone()
            if not primeiros_registros:
                print('\n[AVISO] Nenhuma pessoa cadastrada!')
                return True

            print('\n' + '=' * 45)
            print(f'{"COD":<6} {"NOME":<28} {"ALTURA":>8}')
            print('-' * 45)

            vcod, vnome, valtura = primeiros_registros
            print(f'{vcod:<6} {vnome:<28} {valtura:>8.2f}m')

            for vcod, vnome, valtura in cur:
                print(f'{vcod:<6} {vnome:<28} {valtura:>8.2f}m')

            print('=' * 45)

            return True

    except sqlite3.Error as erro:
        print(f'Falha ao listar pessoas: {erro}')
        return False

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    print('\n======= EXCLUIR PESSOA =======')
    lista = listar_pessoas()
    if not lista:
        return False

    entrada_cod = input('\nDigite o código da pessoa que deseja excluir: ').strip()
    if not entrada_cod.isdigit():
        print('[ERRO] Nenhum código foi informado!')
        return False
    vcod = int(entrada_cod)

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute('SELECT nome, altura FROM pessoas WHERE cod = ?;', (vcod,))
            pessoa = cur.fetchone()
            if not pessoa:
                print(f'\n[ERRO] Nenhuma pessoa encontrada com o código "{vcod}".')
                return False

            vnome, valtura = pessoa
            print(f'\nEncontrei registro {vnome} com {valtura:.2f}m de altura.')

            conf = input('Deseja realmente excluir esta pessoa? [S/N]: ').strip().upper()
            if conf != 'S':
                print('\n[AVISO] Exclusão cancelada pelo usuário.')
                return True

            cur.execute('DELETE FROM pessoas WHERE cod = ?;', (vcod,))
            print(f'\n[SUCESSO] Pessoa "{vnome}" excluída com sucesso!')
            return True
            
    except sqlite3.Error as erro:
        print(f'Falha ao buscar pessoa para exclusão: {erro}')
        return False
        
def buscar_por_nome() -> bool:
    print('\n======= BUSCAR PESSOA POR NOME =======')

    termo = input('Digite o nome(ou parte dele para busca): ')
    if not termo:
        print('[AVISO] Nenhum termo foi informado!')
        return False

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute('SELECT cod, nome, altura FROM pessoas WHERE nome LIKE ? ORDER BY nome;', (f'%{termo}%',))

            busca = cur.fetchone()
            if not busca:
                print(f'\n[AVISO] Nenhuma pessoa encontrada com o nome "{termo}".')
                return True

            print('\n' + '=' * 45)
            print(f'{"COD":<6} {"NOME":<28} {"ALTURA":>8}')
            print('-' * 45)

            vcod, vnome, valtura = busca
            print(f'{vcod:<6} {vnome:<28} {valtura:>8.2f}m')

            for vcod, vnome, valtura in cur:
                print(f'{vcod:<6} {vnome:<28} {valtura:>8.2f}m')

            print('=' * 45)
        return True

    except sqlite3.Error as erro:
        print(f'Falha ao buscar pessoa por nome: {erro}')
        return False
