import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('biblioteca de jogos .db')
cursor = conexao.cursor()

#2 - Inserindo dados
cursor.execute(
    """
        INSERT INTO  jogos(nome, ano, nota)
        VALUES ('FIFA', 2025, 9.5);
    """
)
conexao.commit()
conexao.close()
print("Dados inseridos na tabela")