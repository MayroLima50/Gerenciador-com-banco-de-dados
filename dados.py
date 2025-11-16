# dados.py
import sqlite3
from db import DB_NAME # Importa o nome do banco de dados

def adicionar_novo_jogo(nome, ano, nota):
    """Insere um novo jogo no banco de dados."""
    try:
        with sqlite3.connect(DB_NAME) as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO jogos (nome, ano, nota) VALUES (?, ?, ?)",
                (nome, ano, nota)
            )
            return True, f"Jogo '{nome}' adicionado com sucesso!"
    except sqlite3.IntegrityError:
        return False, f"Erro: O jogo '{nome}' já existe."
    except sqlite3.Error as e:
        return False, f"Erro ao adicionar o jogo: {e}"
