import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('biblioteca de jogos .db')

# 2 - Criando o cusror
cursor = conexao.cursor()

# 3 - Criando a tabela filmes
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS jogos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """    
)

# 4 - Fechando a conexão
conexao.close
print("A tabela foi criada")