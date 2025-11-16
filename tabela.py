def criar_tabela_jogos(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS jogos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                ano INTEGER,
                nota REAL
            );
            """
        )
        print("Tabela 'jogos' verificada/criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")

