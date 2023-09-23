import sqlite3 as lite  # Importando SQLite

""" Projeto: Controle de Despesas Pessoal
    @Autor: Wenes Aquino              """
# -------------------------------------------------------------------------S-----

# Criando coneccao
com = lite.connect('dados.db')

# Criando tebela de categoria
with com:
    cur = com.cursor()
    cur.execute(
        "CREATE TABLE Categoria(id INTEGER PRIMATY KEY, nome TEXT)")

# Criando tebela de receita
with com:
    cur = com.cursor()
    cur.execute(
        "CREATE TABLE Receitas(id INTEGER PRIMATY KEY, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

# Criando tebela de gasto
with com:
    cur = com.cursor()
    cur.execute(
        "CREATE TABLE Gastos(id INTEGER PRIMATY KEY, categoria TEXT, retirado_em DATE, valor DECIMAL)")
