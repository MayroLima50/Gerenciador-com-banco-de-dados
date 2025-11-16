# leitura.py
import sqlite3
from db import DB_NAME

def ler_todos_os_jogos():
    """Lê e retorna todos os jogos da tabela, ordenados por nome."""
    try:
        with sqlite3.connect(DB_NAME) as conexao:
            # Usar row_factory para facilitar o acesso aos dados depois
            conexao.row_factory = sqlite3.Row
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM jogos ORDER BY nome")
            jogos = cursor.fetchall()
            return jogos
    except sqlite3.Error as e:
        print(f"Erro ao ler os jogos: {e}")
        return [] # Retorna uma lista vazia em caso de erro
