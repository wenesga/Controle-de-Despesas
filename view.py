import sqlite3 as lite  # Importando SQLite
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Projeto: Controle de Despesas Pessoal
    @Autor: Wenes Aquino              """
# -----------------------------------------------------------------------------

# Criando Coneccao
con = lite.connect('dados.db')

# Inserir Categoria


def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

# Funçoes para Inserir---------------------------------------------------------

# Inserir Receitas


def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionando_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Inserir Gastos


def inserir_gasto(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Funçoes para Deletar---------------------------------------------------------

# Deletar Receitas


def deletar_receitas(i):
    with con:
        cur = con.corsor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)


# Deletar Gastos

def deletar_gastos(i):
    with con:
        cur = con.corsor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)

# Funçao para ver Dados--------------------------------------------------------


# Ver Categorias
def ver_categorias():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens


# Ver Receitas


def ver_Receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

# Ver Gastos


def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens
