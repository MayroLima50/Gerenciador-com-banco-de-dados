import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('netflix.db')
cursor = conexao.cursor()

#2 - Inserindo dados
cursor.execute(
    """
        INSERT INTO  series(nome, ano, nota)
        VALUES ('Breaking Bad', 2008, 9.5);
    """
)
conexao.commit()
conexao.close()
print("Dados inseridos na tabela")