import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo ScrolledText")
        self.janela.minsize(250,250)
        self.janela.maxsize(250, 250)

        #self.scr = tk.Scrollbar(self.janela)
        #self.scr.pack(side=tk.RIGHT, fill=tk.Y)
        #self.txt = tk.Text(self.janela, height=5, yscrollcommand=self.scr.set)
        #self.txt.pack(side=tk.LEFT, fill=tk.BOTH)
        #self.scr.config(command=self.txt.yview)

        self.sct = ScrolledText(self.janela, height=5)
        self.sct.pack(side=tk.LEFT, fill=tk.BOTH)

variavel = tk.Tk()
Tela(variavel)
variavel.mainloop()
