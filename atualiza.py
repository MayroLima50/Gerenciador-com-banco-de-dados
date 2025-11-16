# atualiza.py
import sqlite3
from db import DB_NAME

def atualizar_dados_jogo(id_jogo, nome, ano, nota):
    """Atualiza as informações de um jogo existente."""
    try:
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                """
                UPDATE jogos
                SET nome = ?, ano = ?, nota = ?
                WHERE id = ?
                """,
                (nome, ano, nota, id_jogo)
            )
            return True, "Jogo atualizado com sucesso!"
    except sqlite3.Error as e:
        return False, f"Erro ao atualizar o jogo: {e}"
