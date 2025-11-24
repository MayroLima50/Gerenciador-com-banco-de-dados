import streamlit as st

from db import conectar_bd
from tabela import criar_tabela_jogos
from dados import adicionar_novo_jogo
from leitura import ler_todos_os_jogos
from excluir import excluir_jogo_por_id
from atualiza import atualizar_dados_jogo

st.set_page_config(layout="centered", page_title="Gerenciador de Jogos")
st.title(" Gerenciador de Biblioteca de Jogos")


def inicializar_banco():
    conexao = conectar_bd()
    if conexao:
        criar_tabela_jogos(conexao)
        conexao.close()


inicializar_banco()

with st.expander(" Adicionar Novo Jogo", expanded=True):
    with st.form("form_adicionar", clear_on_submit=True):
        novo_nome = st.text_input("Nome do Jogo")
        novo_ano = st.number_input("Ano de Lançamento", min_value=1970, max_value=2030, step=1, value=2024)
        nova_nota = st.slider("Nota", 0.0, 10.0, 8.0, step=0.1)

        if st.form_submit_button("Adicionar Jogo"):
            if novo_nome:
                sucesso, mensagem = adicionar_novo_jogo(novo_nome, novo_ano, nova_nota)
                if sucesso:
                    st.success(mensagem)
                    st.rerun()
                else:
                    st.error(mensagem)
            else:
                st.warning("O nome do jogo é obrigatório.")

st.divider()

st.header("📚 Jogos na Biblioteca")
jogos = ler_todos_os_jogos()

if not jogos:
    st.info("Sua biblioteca está vazia. Adicione um jogo acima!")
else:
    col1, col2, col3, col4 = st.columns([1, 4, 2, 2])
    col1.markdown("**ID**")
    col2.markdown("**Nome**")
    col3.markdown("**Ano / Nota**")
    col4.markdown("**Ação**")

    for jogo in jogos:
        col1, col2, col3, col4 = st.columns([1, 4, 2, 2])
        with col1:
            st.write(jogo['id'])
        with col2:
            st.write(jogo['nome'])
        with col3:
            st.write(f"{jogo['ano']} ({jogo['nota']})")
        with col4:
            if st.button("🗑️ Excluir", key=f"del_{jogo['id']}", help=f"Excluir {jogo['nome']}"):
                sucesso, mensagem = excluir_jogo_por_id(jogo['id'])
                if sucesso:
                    st.toast(mensagem)
                    st.rerun()
                else:
                    st.error(mensagem)
