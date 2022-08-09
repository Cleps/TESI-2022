import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Treeview TABELA")
        self.janela.geometry('480x280')

        self.frame = tk.Frame(self.janela)
        self.frame.pack()

        colunas = ["Nome", 'CPF', 'Email']

        self.tvw = ttk.Treeview(self.frame,show="headings", columns=colunas)
        self.tvw.pack(side=tk.LEFT)

        #------CABEÇALHO
        self.tvw.heading('Nome', text='Nome')
        self.tvw.heading('CPF', text='CPF')
        self.tvw.heading('Email', text='Email')

        self.tvw.column('Nome', minwidth=0, width=100)
        self.tvw.column('CPF', minwidth=0, width=150)
        self.tvw.column('Email', minwidth=0, width=200)

        self.tvw.insert("", 'end', values=('Nome', 'CPF', 'Email'))
        self.tvw.insert("", 'end', values=('Nome', 'CPF', 'Email'))
        self.tvw.insert("", 'end', values=('Nome', 'CPF', 'Email'))

        self.scr = tk.Scrollbar(self.frame, command=self.tvw.yview).pack(side=tk.RIGHT,fill=tk.Y)

app = tk.Tk()
Tela(app)
app.mainloop()