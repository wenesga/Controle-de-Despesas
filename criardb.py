import sqlite3 as lite  # Importando SQLite
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Projeto: Controle de Despesas Pessoal
    @Autor: Wenes Aquino              """
# -------------------------------------------------------------------------S-----

# Criando coneccao
con = lite.connect('dados.db')

# Criando tebela de categoria
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Categoria(id INTEGER PRIMATY KEY, nome TEXT)")

# Criando tebela de receita
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Receitas(id INTEGER PRIMATY KEY, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

# Criando tebela de gasto
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Gastos(id INTEGER PRIMATY KEY, categoria TEXT, retirado_em DATE, valor DECIMAL)")
