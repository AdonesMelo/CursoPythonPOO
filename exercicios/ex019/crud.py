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
    pass

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_por_nome() -> bool:
    pass
