import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo RadioButton")
        self.janela.minsize(450,300)
        self.v = tk.StringVar(self.janela, "1")
        self.rbt_1 = tk.Radiobutton(self.janela, text="Opção 1", value="1", variable=self.v).pack()
        self.rbt_2 = tk.Radiobutton(self.janela, text="Opção 2", value="2", variable=self.v).pack()
        self.rbt_3 = tk.Radiobutton(self.janela, text="Opção 3", value="3", variable=self.v).pack()
        self.btn_exit = tk.Button(self.janela, text="Sair",bg="red", command=self.janela.destroy).pack()


app = tk.Tk()
Tela(app)
app.mainloop()