import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('biblioteca de jogos .db')
cursor = conexao.cursor()

# 2 - Leitura de dados
dados = cursor.execute("SELECT * FROM jogos")

print(dados.fetchall())