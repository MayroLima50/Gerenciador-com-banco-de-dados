# excluir.py
import sqlite3
from db import DB_NAME

def excluir_jogo_por_id(id_jogo):
    """Deleta um jogo do banco de dados usando o ID."""
    try:
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM jogos WHERE id = ?", (id_jogo,))
            return True, "Jogo deletado com sucesso!"
    except sqlite3.Error as e:
        return False, f"Erro ao deletar o jogo: {e}"
