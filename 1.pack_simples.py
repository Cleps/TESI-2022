import tkinter as tk

class Pack_simples():

    def __init__(self, master):
        self.janela = master
        self.janela.minsize(240,160)
        self.janela.maxsize(240,160)
        self.janela.title("Pack simples")

        self.lbl_top = tk.Label(text='TOPO',bg="yellow",height=4).pack(side=tk.TOP, fill=tk.X)
        self.lbl_dow = tk.Label(text='RODAPÉ', bg='cyan', height=4).pack(side=tk.BOTTOM, fill=tk.X)
        self.lbl_dir = tk.Label(text="ESQUERDA",bg="red",width=15).pack(side=tk.LEFT, fill=tk.X)
        self.lbl_esq = tk.Label(text="DIREITA",bg='green',width=15).pack(side=tk.RIGHT, fill=tk.X)



class Gerenciador_pack():
    def __init__(self,master):
        self.janela = master
        self.janela.geometry("280x320")
        self.janela.title("Gerenciador Pack")

        self.lbl_red =tk.Label(self.janela,  text="Red", bg="red",height=2).pack(fill=tk.X)
        self.lbl_gre =tk.Label(self.janela, text='Green',bg='green',height=2).pack(fill=tk.X)
        self.lbl_blu =tk.Label(self.janela, text='Blue',bg='blue',height=2).pack(fill=tk.X)
        self.lbl_gr1 =tk.Label(self.janela, text='Gray',bg='gray',width=7).pack(side=tk.LEFT,fill=tk.Y)
        self.lbl_gr2 =tk.Label(self.janela, text='Gray',bg='gray',width=7).pack(side=tk.RIGHT,fill=tk.Y)
        self.lbl_cya =tk.Label(self.janela, text='Cyan',bg='cyan').pack()
        self.lbl_mag =tk.Label(self.janela, text='Magenta',bg='magenta').pack()
        self.lbl_yel =tk.Label(self.janela, text='Yellow',bg='yellow').pack()
        self.lbl_bla =tk.Label(self.janela, text='Black',bg='black').pack()


v = tk.Tk()
#Pack_simples(v)
Gerenciador_pack(v)
v.mainloop()
