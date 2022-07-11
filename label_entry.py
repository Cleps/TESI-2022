import tkinter as tk

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo label com Entry")
        self.janela.minsize(300,450)
        #na label primeiro deve ser adicionado "o pai" da variavel, e dps suas opções
        self.lbl_nome = tk.Label(self.janela, text="Nome:", font=("calibre",10,'bold'))
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.janela, width=20).pack()
        self.lbl_senha = tk.Label(self.janela, text="Senha",font=("calibre",10,'bold')).pack()
        self.ent_senha = tk.Entry(self.janela, width=20, show="*").pack()

#pode ser qlqr nome no APP// mainloop na variavel p manter aberto
app = tk.Tk()
Tela(app)
app.mainloop()