import tkinter as tk
from tkinter import ttk
class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Combobox")
        self.janela.minsize(250,250)
        self.janela.maxsize(250, 250)
        self.scr = tk.Scrollbar(self.janela)
        self.scr.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt = tk.Text(self.janela, height=5, yscrollcommand=self.scr.set)
        self.txt.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scr.config(command=self.txt.yview)


variavel = tk.Tk()
Tela(variavel)
variavel.mainloop()


