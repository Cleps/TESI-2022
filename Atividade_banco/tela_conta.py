from re import S
import tkinter as tk
from tkinter import SCROLL, messagebox, ttk
from interface import *


class TelaConta:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('350x300')
        self.janela.title('Cadastro de Cliente')

        self.frm_top = tk.Frame(self.janela)
        self.frm_top.pack(side=tk.TOP)

        self.lbl_nom = tk.Label(self.frm_top, text='Numero:')
        self.lbl_nom.grid(row=0, column=0)
        self.lbl_cliente = tk.Label(self.frm_top, text='cliente:')
        self.lbl_cliente.grid(row=1, column=0)
        self.ent_nom = tk.Entry(self.frm_top, width=20)
        self.ent_nom.grid(row=0, column=1)
        self.ent_cliente = tk.Entry(self.frm_top, width=20)
        self.ent_cliente.grid(row=1, column=1)
        self.ent_cliente['state'] = tk.DISABLED
        self.btn_cnf = tk.Button(self.frm_top, text='CONFIRMAR', command=self.inserir)
        self.btn_cnf.grid(row=2, column=1)

        create_table_banco()
        # ----------------------------------------------------------------------

        self.frm_bot = tk.Frame(self.janela)
        self.frm_bot.pack(side=tk.BOTTOM)

        colunas = ['Id', 'Numero', 'cliente','saldo']
        self.tvw_cli = ttk.Treeview(self.frm_bot, columns=colunas, height=8, show='headings')
        self.tvw_cli.grid(row=0, column=0, columnspan=2)

        self.tvw_cli.heading('Id', text='Id')
        self.tvw_cli.column('Id', minwidth=0, width=30)
        self.tvw_cli.heading('Numero', text='Numero')
        self.tvw_cli.column('Numero', minwidth=0, width=80)
        self.tvw_cli.heading('cliente', text='cliente')
        self.tvw_cli.column('cliente', minwidth=0, width=150)
        self.tvw_cli.heading('saldo', text='saldo')
        self.tvw_cli.column('saldo', minwidth=0, width=50)


        self.scr = tk.Scrollbar(self.frm_bot, command=self.tvw_cli.yview, width=20)
        self.scr.grid(row=0, column=2, sticky=tk.NS)
        self.tvw_cli.configure(yscrollcommand=self.scr.set)

        self.atualizar_tvw()

        self.btn_att = tk.Button(self.frm_bot, text='ATUALIZAR CLIENTE', command=self.atualizar_cliente)
        self.btn_att.grid(row=1, column=1)

        self.btn_del = tk.Button(self.frm_bot, text='DELETAR', command=self.deletar)
        self.btn_del.grid(row=1, column=0)

        self.btn_pesquisar = tk.Button(self.frm_bot, text='PESQUISAR', command=self.pesquisar)
        self.btn_pesquisar.grid(row=1, column=2)

    def pesquisar(self):
        self.top = tk.Toplevel(self.janela)
        self.top.geometry('280x300')

        self.lbl_clientetop = tk.Label(self.top, text='cliente:')
        self.lbl_clientetop.grid(row=0, column=0)
        self.ent_clientetop = tk.Entry(self.top, width=20)
        self.ent_clientetop.grid(row=0, column=1)

        self.btn_pesquisartop = tk.Button(self.top, text='PESQUISAR', command=self.pesquisar_cliente)
        self.btn_pesquisartop.grid(row=1, column=1)

        ### TREEVIEW ###
        colunas = ['Id', 'Numero', 'cliente']
        self.tvw_clitop = ttk.Treeview(self.top, columns=colunas, height=8, show='headings')
        self.tvw_clitop.grid(row=2, column=0, columnspan=2)

        self.tvw_clitop.heading('Id', text='Id')
        self.tvw_clitop.column('Id', minwidth=0, width=30)
        self.tvw_clitop.heading('Numero', text='Numero')
        self.tvw_clitop.column('Numero', minwidth=0, width=60)
        self.tvw_clitop.heading('cliente', text='cliente')
        self.tvw_clitop.column('cliente', minwidth=0, width=100)


        self.btn_selecionar = tk.Button(self.top, text='SELECIONAR', command=self.selecionar)
        self.btn_selecionar.grid(row=3, column=1)
# -------------- FUNÇÃO DE PESQUISAR ------------------------------------------------------------

    def pesquisar_cliente(self):
        nome = self.ent_clientetop.get()
        sql = f'''SELECT *  
        FROM clientes cli 
        WHERE cli.nome LIKE "%{nome}%" ''' #pode ser nome, outros dados
        dados = executar(sql)
        print(dados)
        for i in self.tvw_clitop.get_children():  # deleto todos q tiverem na treeview para nao repetir
            self.tvw_clitop.delete(i)
        for any in dados:  # insiro conforme dados do db
            self.tvw_clitop.insert('', 'end', values=(any[0], any[1], any[2]))

    def selecionar(self):
        selecionado = self.tvw_clitop.selection()
        nome = self.tvw_clitop.item(selecionado, 'values')[1]
        self.ent_cliente['state'] = tk.NORMAL
        self.ent_cliente.insert(0, nome)
        self.top.destroy()

    def inserir(self):
        nome = self.ent_nom.get()
        cpf = self.ent_cpf.get()
        if nome == '' or cpf == '':
            messagebox.showerror('ERRO', 'Nenhum campo pode estar vazio')
        else:
            inserir_banco(nome, cpf)
            messagebox.showinfo('Concluido!', 'Cliente inserido com sucesso!')
            self.atualizar_tvw()
            self.ent_cpf.delete(0, 'end')
            self.ent_nom.delete(0, 'end')

    def deletar(self):
        selecionado = self.tvw_cli.selection()
        if len(selecionado) == 1:
            itens = self.tvw_cli.item(selecionado, 'values')
            deletar(itens[0])
            self.tvw_cli.delete(selecionado)
        else:
            messagebox.showerror('ERRO!', 'Selecione apenas UM cliente blz?')

    def atualizar_cliente(self):
        cpf = self.ent_cpf.get()
        nome = self.ent_nom.get()
        selecionado = self.tvw_cli.selection()

        if len(selecionado) == 1 and cpf != '' and nome != '':
            itens = self.tvw_cli.item(selecionado, 'values')
            atualizar(itens[0], nome, cpf)
            self.tvw_cli.item(selecionado, values=(itens[0], nome, cpf))
            self.ent_cpf.delete(0, 'end')
            self.ent_nom.delete(0, 'end')

        else:
            messagebox.showerror('ERRO!',
                                 'Selecione apenas UM cliente blz?\nAlém disso, nenhum dos campos pode ficar vazio.')

    def atualizar_tvw(self):
        dados = consultar_contas()
        for i in self.tvw_cli.get_children():  # deleto todos q tiverem na treeview para nao repetir
            self.tvw_cli.delete(i)
        for any in dados:  # insiro conforme dados do db
            self.tvw_cli.insert('', 'end', values=(any[0], any[1], any[2], any[3]))


app = tk.Tk()
TelaConta(app)
app.mainloop()