import tkinter as tk

#Os comandos pra iniciar cada janela tão lá embaixo, acho q fica melhor somente um arquivo
#Inclusive eu tenho uma duvida qnto aos comandos do menu, tk.Menu e barras e tudo mais, pelo jeito
#não tem como gerenciar com o pack, grid e outros, como faço p gerenciar o layout dos menus ent?
#Já aproveitando, aquele final de aula sobre menus ficou mt curtinho, se puder passar mais conteudo sobre, agradeço

class Pack_simples:

    def __init__(self, master):
        self.janela = master
        self.janela.minsize(240, 160)
        self.janela.maxsize(240, 160)
        self.janela.title("Pack simples")

        self.lbl_top = tk.Label(text='TOPO', bg="yellow", height=4).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.lbl_dow = tk.Label(text='RODAPÉ', bg='cyan', height=4).pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.lbl_dir = tk.Label(text="ESQUERDA", bg="red", width=15).pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.lbl_esq = tk.Label(text="DIREITA", bg='green', width=15).pack(side=tk.RIGHT, fill=tk.X, expand=True)

#----------------------------------------------------------------------------------------------------------------------------

#Esse ficou brabo, coloquei ate a corzinha da letra branco, nn foi especificado se a janela devia ser fixa então fiz a gosto
#Eu ia colocar o .pack() em outras linhas mas acho mais bonito o code com menos linhas

class Gerenciador_pack:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("290x290")
        self.janela.title("Gerenciador Pack")

        self.lbl_red = tk.Label(self.janela, text="Red", bg="red",fg='white', height=2).pack(fill=tk.X)
        self.lbl_gre = tk.Label(self.janela, text='Green', bg='green',fg='white', height=2).pack(fill=tk.X)
        self.lbl_blu = tk.Label(self.janela, text='Blue', bg='blue',fg='white', height=2).pack(fill=tk.X)
        self.lbl_gr1 = tk.Label(self.janela, text='Gray', bg='gray',fg='white', width=7).pack(side=tk.LEFT, fill=tk.Y)
        self.lbl_gr2 = tk.Label(self.janela, text='Gray', bg='gray',fg='white', width=7).pack(side=tk.RIGHT, fill=tk.Y)
        self.lbl_bla = tk.Label(self.janela, text='Black', bg='black',fg='white').pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        self.lbl_cya = tk.Label(self.janela, text='Cyan', height=2, bg='cyan').pack(anchor=tk.NW,side=tk.LEFT,fill=tk.X, expand=True)
        self.lbl_yel = tk.Label(self.janela, text='Yellow', bg='yellow', height=2).pack(anchor=tk.NE,side=tk.RIGHT,fill=tk.X, expand=True)
        self.lbl_mag = tk.Label(self.janela, text='Magenta', bg='magenta',width=10, height=2).pack(fill=tk.BOTH)

#----------------------------------------------------------------------------------------------------------------------------------------

class Soma_simples:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("240x120")
        self.janela.minsize(240, 120)
        self.janela.title("Soma Simples")

        self.lbl_1 = tk.Label(self.janela,text="Número 1:").grid(row=0,column=0,padx=5, pady=5)
        self.lbl_2 = tk.Label(self.janela,text="Número 2:").grid(row=1,column=0,padx=5, pady=5)
        self.ent_1 = tk.Entry(self.janela).grid(row=0, column=1,padx=5, pady=5)
        self.ent_2 = tk.Entry(self.janela).grid(row=1, column=1,padx=5, pady=5)
        self.btn_som = tk.Button(self.janela,text="Somar >>").grid(row=2, column=0,padx=5, pady=5)
        #Nn tenho certeza se o proximo devia ser uma label com um texto ou nn, mas creio q seja possivel
        self.lbl_sai = tk.Label(self.janela, text="0.3", bg="white", width=15).grid(row=2,column=1)


#----------------------------------------------------------------------------------------------------------------------------------------


class Gerenciador_grid:
    def __init__(self, master):
        self.janela = master
        self.janela.minsize(230, 130)
        self.janela.maxsize(230, 130)
        self.janela.title("Gerenciador Grid")
#rapaz eu nn gosto, mas tive de fazer gambiarra cm essa label fantasma aq pq esse gerenciador de grid é mt ruim pra isso

        self.lbl_fantasma = tk.Label(self.janela, text='', width=5, height=2).grid(row=0, column=0)
        self.btn_1 = tk.Button(self.janela, text="1", width=5, height=2).grid(row=0, column=2)
        self.btn_2 = tk.Button(self.janela, text="2", width=5, height=2).grid(row=1, column=1, columnspan=2)
        self.btn_3 = tk.Button(self.janela, text="3", width=5, height=2).grid(row=1, column=2, columnspan=3)
        self.btn_4 = tk.Button(self.janela, text="4", width=5, height=2).grid(row=2, column=1)
        self.btn_5 = tk.Button(self.janela, text="5", width=5, height=2).grid(row=2, column=2)
        self.btn_6 = tk.Button(self.janela, text="6", width=5, height=2).grid(row=2, column=3)

#-------------------------------------------------------------------------------------------------------------------

v = tk.Tk()

#Pack_simples(v)
#Gerenciador_pack(v)
#Soma_simples(v)
#Gerenciador_grid(v)

v.mainloop()

#Tem algum modo de fazer abrir a janela direto da classe? tipo chamando "Tela()" e ja abre direto sem precisar dessas 3 linhas acima
#GGEZ