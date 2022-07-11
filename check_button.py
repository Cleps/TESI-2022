import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo checkbutton")
        self.janela.minsize(450,300)

        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar()
        
        self.ckb_1 = tk.Checkbutton(self.janela, text="Opção 1", variable=self.v1,bg="blue").pack()
        self.ckb_1 = tk.Checkbutton(self.janela, text="Opção 2", variable=self.v2,bg="green").pack()


app = tk.Tk()
Tela(app)
app.mainloop()