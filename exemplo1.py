from re import T
import tkinter as tk

janela = tk.Tk()
janela.geometry("300x250")


'''
def menu(event):
    barra = tk.Menu(janela)
    menu = tk.Menu(barra)
    barra.add_cascade(label = "Menu", menu=menu)
    menu.add_separator() #--------------------------------------linha separadora opcional
    menu.add_command(label = 'Contas (provisorio)')
    menu.add_command(label = 'Clientes (provisorio)')
    menu.add_command(label = 'Bancos (provisorio)')
    janela.config(menu=barra)
'''
 
#-----------------esta função é do tipo event
def clicou(event):
    lbl = tk.Label(janela, text=f"VOCE CLICOU NO BUTÃO {event.keysym}")
    lbl.pack(side=tk.TOP)

btn = tk.Button(janela, text="CLIQUE AQUI!")
#-------------adcionando event para o btn
btn.bind('<Button-3>', clicou)
#---------------a partir do segundo add um "+"
btn.bind('<Button-1>', clicou, add="+")
btn.focus()
btn.pack()
btn.bind('<Any-KeyPress>', clicou, add="+")


janela.mainloop()