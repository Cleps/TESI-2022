import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Menu")
        self.barra = tk.Menu(self.janela)

        self.barra2 = tk.Menu(self.janela)
        self.menu2 = tk.Menu(self.barra2)
        
        self.menu1 = tk.Menu(self.barra)
        self.barra.add_cascade(label = "Arquivo", menu=self.menu1)
        self.menu1.add_separator()
        self.menu1.add_command(label = 'Abrir')
        self.menu1.add_command(label = 'Salvar')
        self.menu1.add_command(label = 'Exportar')
        self.janela.config(menu=self.barra)

variavel = tk.Tk()
Tela(variavel)
variavel.mainloop()

