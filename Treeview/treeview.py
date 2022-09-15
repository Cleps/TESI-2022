import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Treeview")
        self.janela.geometry('360x500')

        self.tvw = ttk.Treeview(self.janela)
        self.tvw.pack()

        self.tvw.insert("", 'end', text="alunos")
        self.tvw.insert("", 'end', text="Seres Humanos")
        self.tvw.insert("", 'end', text="Professores")
        id_Capivaras = self.tvw.insert("", 'end', text="Capivaras")
        self.tvw.insert(id_Capivaras, 'end', text="Capivarinhas")
        self.tvw.insert(id_Capivaras, 'end', text="Capivaroas")
        self.tvw.insert(id_Capivaras, 'end', text="Capivarãos")



app = tk.Tk()
Tela(app)
app.mainloop()
