import sqlite3

# 1 - Conectando no BF
conexao = sqlite3.connect('biblioteca de jogos .db')
cursor = conexao.cursor()

# 2 - Exclusão de dados
id = 1, 2
cursor.execute(
    """
        DELETE FROM jogos
        WHERE id in (?, ?)
    """,
    id
)

conexao.commit()
print("Dados excluídos com sucesso")