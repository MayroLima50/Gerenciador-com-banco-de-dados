import sqlite3

# 1 - Conectando no BF
conexao = sqlite3.connect('biblioteca de jogos .db')
cursor = conexao.cursor()

# 2 - Atualiza dados
id = 1
cursor.execute(
    """
        UPDATE series SET nome = ?
        WHERE id = ?
    """,
    ("gow of war", id)
)

conexao.commit()
print("Dados atualizados!")