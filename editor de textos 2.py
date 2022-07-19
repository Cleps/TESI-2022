import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('640x320')
        self.janela.title("Exemplo Menu")

        self.barra = tk.Menu(self.janela)
        self.menu1 = tk.Menu(self.barra)

        self.barra2 = tk.Menu(self.janela)
        self.menu2 = tk.Menu(self.barra2)        
        
        self.barra.add_cascade(label = "Arquivo", menu=self.menu1)
        self.barra.add_cascade(label = "Sair", menu=self.menu2)
        self.menu2.add_command(label = "Sair", command=self.janela.destroy)
        #self.menu1.add_separator()
        self.menu1.add_command(label = 'Abrir')
        self.menu1.add_command(label = 'Salvar')
        self.menu1.add_command(label = 'Exportar')
        self.janela.config(menu=self.barra)

      

        self.btn = tk.Button(self.janela, text='sair', command=self.janela.destroy)
        self.btn.pack(side=tk.RIGHT)

        self.scr = tk.Scrollbar(self.janela)
        self.scr.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt = tk.Text(self.janela, height=10,width=200, yscrollcommand=self.scr.set)
        self.txt.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scr.config(command=self.txt.yview)

variavel = tk.Tk()
Tela(variavel)
variavel.mainloop()
