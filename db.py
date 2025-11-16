
import sqlite3

DB_NAME = 'biblioteca_de_jogos.db'

def conectar_bd():
    try:
        conexao = sqlite3.connect(DB_NAME)
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

