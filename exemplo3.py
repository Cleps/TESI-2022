import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


janela = tk.Tk()
janela.geometry("300x250")

lista = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sextou', 'Sabado']

def selecionado(event):
    if cbx.get() == "Sextou":
        messagebox.showinfo('', 'SEXTOUUUUUUUUUUU')
    else:
        messagebox.showinfo('INFO', f'{cbx.get()}')

cbx = ttk.Combobox(janela, values= lista)
cbx.bind('<<ComboboxSelected>>', selecionado)
cbx.pack()


janela.mainloop()