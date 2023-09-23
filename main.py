from tkinter import messagebox
from tkinter import *
from tkinter import Tk, StringVar, ttk

""" Projeto: Controle de Despesas Pessoal
    @Autor: Wenes Aquino              """
# ------------------------------------------------------------------------------
# ================= cores =================
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

# ================= criando janela =================
janela = Tk()
janela.title("")
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0,
                font=('Calibri', 9))  # Modify the font of the body

janela.mainloop()

# ================= Frames =================
frameCima = Frame(janela, width=1043, height=50, bg=co1,  relief="flat",)
frameCima.grid(l=0, column=0)

frameMeio = Frame(janela, width=1043, height=361,
                  bg=co1, pady=20, relief="raised")
frameMeio.grid(l=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(l=2, column=0, pady=0, padx=10, sticky=NSEW)

frame_gra_2 = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_2.place(x=415, y=5)

# abrindo imagem
app_img = Image.open('log.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT,
                 padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)

app_logo.place(x=0, y=0)
