import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Primeira Janela")
        self.janela.minsize(600,400)
        self.janela.geometry("600x400")
        self.container = tk.Frame(self.janela)
        self.container.pack()

        self.lbl = tk.Label(self.container, text="Primeiro texto", bg="red")
        self.lbl.configure(font=("Verdana", "40"))
        self.lbl.pack()


janelaprincipal = tk.Tk()
Tela(janelaprincipal)
janelaprincipal.mainloop()
