import tkinter as tk
from tkinter import ttk
class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Combobox")
        v = tk.StringVar()
        self.janela.minsize(400,250)
        self.cbx = ttk.Combobox(self.janela, textvariable=v)
        self.cbx['values'] = ('Domingo','Segunda','Terça')
       # self.current(1)
        self.cbx.pack()


variavel = tk.Tk()
Tela(variavel)
variavel.mainloop()


