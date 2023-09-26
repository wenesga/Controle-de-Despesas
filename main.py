import tkinter as tk
from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Importando barra de progresso Tkinter
from tkinter.ttk import Progressbar

# Importando Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


# tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

""" Projeto: Controle de Despesas Pessoal
    @Autor: Wenes Aquino              """
# ------------------------------------------------------------------------------
# ================= cores =================
co0 = "#2e2d2b"   # Preta
co1 = "#ffffff"   # branca
co2 = "#4fa882"   # verde
co3 = "#38576b"   # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

co10 = "#68c985"  # Verde

#           azul     vermelho     verde
colors = ['#4583de', '#ff5747', '#68c985', '#ee9944', '#444466', '#bb5555']

# ================= criando janela =================


janela = Tk()

# Icone do aplicativo e da barra de titulo


janela.title("Minhas Finanças")
janela.geometry('900x670')
janela.configure(background=co1)
janela.iconbitmap('icone.ico')

# Bloqueia o redimensionamento da janela
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("default")  # Tema
style.configure("Treeview", highlightthickness=0, bd=0,
                font=('Geometria', 9))  # Modifique a fonte do corpo


# ================= Frames Cima =================
frameCima = Frame(janela, width=1043, height=50, bg=co1,  relief="flat",)
frameCima.grid(row=0, column=0)

# ================= Frames Meio =================
frameMeio = Frame(janela, width=1043, height=361,
                  bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# ================= Frames Baixo ================
frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

# ================= Frames Grafico ================
frame_gra_2 = Frame(frameMeio, width=580, height=250, bg=co1)
frame_gra_2.place(x=415, y=5)


# Acessando Imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Minhas Finanças", width=900, compound=LEFT,
                 padx=5, relief=RAISED, anchor=NW, font=('Geometria 16 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)


global tree

# funcao inserir


def inserir():
    global imagem, imagem_string, l_imagem
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_form(lista_inserir)
    messagebox.showinfo(
        'Sucesso', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0, 'end')

    for widget in frameDireita.winfo_children():
        widget.destroy()

    mostrar()

# funcao atualizar


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serial.delete(0, 'end')

        id = int(treev_lista[0])

        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serial.insert(0, treev_lista[7])

        def update():
            global imagem, imagem_string, l_imagem
            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serial.get()
            imagem = imagem_string

            if imagem == '':
                imagem = e_serial.insert(0, treev_lista[7])

            lista_atualizar = [nome, local, descricao,
                               model, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            atualizar_form(lista_atualizar)

            messagebox.showinfo(
                'Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serial.delete(0, 'end')

            botao_confirmar.destroy()

            for widget in frameDireita.winfo_children():
                widget.destroy()

            mostrar()

        botao_confirmar = Button(frameMeio, command=update, text="Confirmar".upper(
        ), width=13, height=1, bg=co2, fg=co1, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


# funcao deletar

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frameDireita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


# funcao para abrir imagem
def ver_imagem():
    global l_imagem, imagem, imagem_string

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']
    valor = [int(treev_lista[0])]

    iten = ver_iten(valor)

    imagem = iten[0][8]

    # abrindo a imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)


# percentagem ------------------------------------


def percentagem():
    l_nome = Label(frameMeio, text="Total Gasto",
                   height=1, anchor=NW, font=('Geometria 12 '), bg=co1, fg=co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')

    valor = 30
    # print(valor)

    if valor > 50:
        style.configure("black.Horizontal.TProgressbar", background='#ff5747')
    else:
        style.configure("black.Horizontal.TProgressbar", background=co10)

    style.configure("TProgressbar", thickness=20)

    bar = Progressbar(frameMeio, length=180,
                      style='black.Horizontal.TProgressbar')

    bar.place(x=10, y=35)
    bar['value'] = 50

    l_percentagem = Label(frameMeio, text='{:,.2f} %'.format(
        valor), height=1, anchor=NW, font=('Geometria 12 '), bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)


# funcao para grafico bar ------------------------

def grafico_bar():

    # obtendo valores de meses
    lista_categorias = ['Salário', 'Despesa', 'Saldo']
    lista_valores = [1000, 300, 700]

    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)

    # ax.autoscale(enable=True, axis='both', tight=None)
    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)

    # create a list to collect the plt.patches data
    c = 0

    # definir rótulos de barras individuais usando a lista acima
    for i in ax.patches:
        # get_x puxa para a esquerda ou para a direita; get_height empurra para cima ou para baixo
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom', color='dimgrey')

        c += 1

    ax.set_xticklabels(lista_categorias, fontsize=16)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)


# -----------------------------------------------------------------------------------------
# funcao de resumo total
def resumo():

    valor = [1000, 300, 700]

    l_linha = Label(frameMeio, text="", width=215, height=1,
                    anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=54)  # Traço em baixo do texto Salário

    l_sumario = Label(frameMeio, text="Salário                                    ".upper(
    ), height=1, anchor=NW, font=('Geometria 12'), bg=co1, fg='#4583de')
    l_sumario.place(x=306, y=35)

    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(
        valor[0]), height=1, anchor=NW, font=('arial 15 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1,
                    anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=134)  # Traço em baixo do texto Despesas

    l_sumario = Label(frameMeio, text="Despesas                                  ".upper(
    ), height=1, anchor=NW, font=('Geometria 12'), bg=co1, fg='#ff5747')
    l_sumario.place(x=306, y=115)

    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(
        valor[1]), height=1, anchor=NW, font=('arial 15 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=150)

    l_linha = Label(frameMeio, text="", width=215, height=1,
                    anchor=NW, font=('arial 1 '), bg='#545454',)
    l_linha.place(x=309, y=209)  # Traço em baixo do texto Saldo

    l_sumario = Label(frameMeio, text="Saldo                                        ".upper(
    ), height=1, anchor=NW, font=('Geometria 12'), bg=co1, fg='#68c985')
    l_sumario.place(x=306, y=190)

    l_sumario = Label(frameMeio, text='R$ {:,.2f}'.format(
        valor[2]), height=1, anchor=NW, font=('arial 15 '), bg=co1, fg='#545454')
    l_sumario.place(x=306, y=220)


# ----------------------------------------------------------------------------------------

# funcao grafico pie
def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    lista_valores = [345, 225, 534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = []
    for i in lista_categorias:
        explode.append(0.05)
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2),
           autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right",
              bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_2)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


frame_renda = Frame(frameBaixo, width=300, height=250, bg=co1)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_operacoes.grid(row=0, column=1, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_configuracao.grid(row=0, column=2, padx=5)


# Tabela Renda mensal ---------------------------------------------------------
l_income = Label(frameMeio, text="Tabela Receitas e Despesas",
                 height=1, anchor=NW, font=('Geometria 12'), bg=co1, fg=co4)
l_income.place(x=5, y=309)

# funcao para mostrar_renda


def mostrar_renda():
    # criando uma visualização em árvore com barras de rolagem duplas
    tabela_head = ['Item', 'Categoria', 'Data', 'Quantidade']

    lista_itens = [[0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4],
                   [0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4],
                   [0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4]]

    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",
                        columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd = ["center", "center", "center", "center"]
    h = [30, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


percentagem()
grafico_bar()
resumo()
grafico_pie()
mostrar_renda()
janela.mainloop()


# # Configuracoes Despesas -----------------------------------
# l_descricao = Label(frame_operacoes, text="Insira novas despesas", height=1,
#                     anchor=NW, relief="flat", font=('Geometria 10 bold'), bg=co1, fg=co4)
# l_descricao.place(x=10, y=10)

# l_descricao = Label(frame_operacoes, text="Categoria", height=1,
#                     anchor=NW, relief="flat", font=('Ivy 10'), bg=co1, fg=co4)
# l_descricao.place(x=10, y=40)

# # Pegando os categorias
# categorias_funcao = ['viagens', 'comida']
# categorias = []

# for i in categorias_funcao:
#     categorias.append(i[1])

# combo_categoria_despesas = ttk.Combobox(
#     frame_operacoes, width=10, font=('Ivy 10'))
# combo_categoria_despesas['values'] = (categorias)
# combo_categoria_despesas.place(x=110, y=41)

# l_cal_despeas = Label(frame_operacoes, text="Data", height=1,
#                       anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
# l_cal_despeas.place(x=10, y=70)

# e_cal_despeas = DateEntry(frame_operacoes, width=12, background='darkblue',
#                           foreground='white', borderwidth=2, year=2020)
# e_cal_despeas.place(x=110, y=71)

# l_valor_despesas = Label(frame_operacoes, text="Quantia Total",
#                          height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
# l_valor_despesas.place(x=10, y=100)
# e_valor_despesas = Entry(frame_operacoes, width=14,
#                          justify='left', relief="solid")
# e_valor_despesas.place(x=110, y=101)

# # Botao Inserir
# img_add_despesas = Image.open('add.png')
# img_add_despesas = img_add_despesas.resize((17, 17))
# img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

# botao_inserir_despesas = Button(frame_operacoes, image=img_add_despesas, compound=LEFT, anchor=NW,
#                                 text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'), bg=co1, fg=co0)
# botao_inserir_despesas.place(x=110, y=131)


# # operacao Excluir -----------------------
# l_n_categoria = Label(frame_operacoes, text="Excluir ação",
#                       height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
# l_n_categoria.place(x=10, y=190)


# # Botao Deletar
# img_delete = Image.open('delete.png')
# img_delete = img_delete.resize((20, 20))
# img_delete = ImageTk.PhotoImage(img_delete)
# botao_deletar = Button(frame_operacoes, image=img_delete, compound=LEFT, anchor=NW,
#                        text="   Deletar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'), bg=co1, fg=co0)
# botao_deletar.place(x=110, y=190)

# # Configuracoes Receitas -----------------------------------

# l_descricao = Label(frame_configuracao, text="Insira novas receitas", height=1,
#                     anchor=NW, relief="flat", font=('Geometria 10 bold'), bg=co1, fg=co4)
# l_descricao.place(x=10, y=10)

# l_cal_receitas = Label(frame_configuracao, text="Data",
#                        height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
# l_cal_receitas.place(x=10, y=40)
# e_cal_receitas = DateEntry(frame_configuracao, width=12,
#                            background='darkblue', foreground='white', borderwidth=2, year=2020)
# e_cal_receitas.place(x=110, y=41)

# l_valor_receitas = Label(frame_configuracao, text="Quantia Total",
#                          height=1, anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
# l_valor_receitas.place(x=10, y=70)
# e_valor_receitas = Entry(frame_configuracao, width=14,
#                          justify='left', relief="solid")
# e_valor_receitas.place(x=110, y=71)

# # Botao Inserir
# img_add_receitas = Image.open('add.png')
# img_add_receitas = img_add_receitas.resize((17, 17))
# img_add_receitas = ImageTk.PhotoImage(img_add_receitas)
# botao_inserir_receitas = Button(frame_configuracao, image=img_add_receitas, compound=LEFT, anchor=NW,
#                                 text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'), bg=co1, fg=co0)
# botao_inserir_receitas.place(x=110, y=111)


# # operacao Nova Categoria -----------------------

# l_n_categoria = Label(frame_configuracao, text="Categoria",
#                       height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
# l_n_categoria.place(x=10, y=160)
# e_n_categoria = Entry(frame_configuracao, width=14,
#                       justify='left', relief="solid")
# e_n_categoria.place(x=110, y=160)

# # Botao Inserir
# img_add_categoria = Image.open('add.png')
# img_add_categoria = img_add_categoria.resize((17, 17))
# img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
# botao_inserir_categoria = Button(frame_configuracao, image=img_add_categoria, compound=LEFT, anchor=NW,
#                                  text=" Adicionar".upper(), width=80, overrelief=RIDGE,  font=('ivy 7 bold'), bg=co1, fg=co0)
# botao_inserir_categoria.place(x=110, y=190)
