from re import S
import tkinter as tk
from tkinter import SCROLL, messagebox, ttk
from interface import *

#o banco precisa ter um ID autoincrement
#chamar o att treview qndo inserir

class TelaCliente:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('420x420')
        self.janela.title('Cadastro de Cliente')

        self.frm_top = tk.Frame(self.janela)
        self.frm_top.pack(side=tk.TOP)

        self.lbl_nom = tk.Label(self.frm_top, text='Nome:')
        self.lbl_nom.grid(row=0,column=0)
        self.lbl_cpf = tk.Label(self.frm_top, text='CPF:')
        self.lbl_cpf.grid(row=1,column=0)
        self.ent_nom = tk.Entry(self.frm_top, width=20)
        self.ent_nom.grid(row=0,column=1)
        self.ent_cpf = tk.Entry(self.frm_top, width=20)
        self.ent_cpf.grid(row=1, column=1)
        self.btn_cnf = tk.Button(self.frm_top, text='CONFIRMAR', command=self.inserir)
        self.btn_cnf.grid(row=2, column=1)

        create_table_banco()
#----------------------------------------------------------------------
        
        self.frm_bot = tk.LabelFrame(self.janela)
        self.frm_bot.pack(side=tk.BOTTOM)

        colunas = ['Nome', 'CPF']
        self.tvw_cli = ttk.Treeview(self.frm_bot, columns=colunas, height=8, show='headings')
        self.tvw_cli.grid(row=0, column=0)

        self.tvw_cli.heading('Nome', text='Nome')
        self.tvw_cli.column('Nome', minwidth=0, width=100)
        self.tvw_cli.heading('CPF', text='CPF')
        self.tvw_cli.column('CPF', minwidth=0, width=100)

        self.scr = tk.Scrollbar(self.frm_bot, command=self.tvw_cli.yview, width=25)
        self.scr.grid(row=0, column=1, sticky=tk.NS)
        self.scr.configure(SCROLL=self.tvw_cli)

        self.btn_att = tk.Button(self.frm_bot, text='Atualizar tabela')
        self.btn_att.grid(row=1, column=0)


    def inserir(self):
        nome = self.ent_nom.get()
        cpf = self.ent_cpf.get()
        if nome=='' or cpf=='':
            messagebox.showerror('ERRO', 'Nenhum campo pode estar vazio')
        else:
            inserir_banco(nome, cpf)
            messagebox.showinfo('Concluido!', 'Cliente inserido com sucesso!')



        



app = tk.Tk()
TelaCliente(app)
app.mainloop()