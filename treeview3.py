import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Treeview TABELA")
        self.janela.geometry('480x280')
#-------------FRAME PADRÃO
        self.frame = tk.Frame(self.janela)
        self.frame.pack(side=tk.TOP)
#------------FRAME DE BOTÕES
        self.btn_frm = tk.Frame(self.janela)
        self.btn_frm.pack(side=tk.BOTTOM)

        colunas = ["Nome", 'CPF', 'Email']

        self.tvw = ttk.Treeview(self.frame,show="headings", columns=colunas)
        self.tvw.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

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
        


#-----------SCROLLBAR
        self.scr = tk.Scrollbar(self.frame, command=self.tvw.yview).pack(side=tk.RIGHT,fill=tk.Y)

#------------BOTÕES NO FRAME BOTOES

        self.btn_cad = tk.Button(self.btn_frm, text="Cadastrar", command=self.tela_cadastrar)
        self.btn_cad.pack()


    def tela_cadastrar(self):
        

        self.top_cadastro = tk.Toplevel(self.janela)
        self.top_cadastro.title("cadastro")
        self.top_cadastro.geometry("300x120")
        
        self.janela.withdraw()
        #self.top_cadastro.grab_set()        

        self.lbl_nam = tk.Label(self.top_cadastro, text="Nome:")
        self.lbl_nam.grid(row=0, column=0)

        self.ent_nam = tk.Entry(self.top_cadastro)
        self.ent_nam.grid(row=0,column=1)

        self.lbl_cpf = tk.Label(self.top_cadastro,text="CPF:")
        self.lbl_cpf.grid(row=1, column=0)

        self.ent_cpf = tk.Entry(self.top_cadastro)
        self.ent_cpf.grid(row=1,column=1)

        self.lbl_ema = tk.Label(self.top_cadastro, text="Email:")
        self.lbl_ema.grid(row=2,column=0)
        
        self.ent_ema = tk.Entry(self.top_cadastro)
        self.ent_ema.grid(row=2,column=1)

        self.btn_cnf = tk.Button(self.top_cadastro, text="Confirmar",command=self.confirmar_cadastro)
        self.btn_cnf.grid(row=3,column=0)

        

    def confirmar_cadastro(self):
        if self.ent_nam.get() == '' or self.ent_cpf.get() == '' or self.ent_ema.get()=='':
            messagebox.showwarning("ERRO!!!!!", "Nenhum dos campos pode ficar vazio!")
        else:
            self.tvw.insert("","end",values=(self.ent_nam.get(),self.ent_cpf.get(), self.ent_ema.get()))
            self.top_cadastro.destroy()
            self.janela.deiconify()



app = tk.Tk()
Tela(app)
app.mainloop()
