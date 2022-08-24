import tkinter as tk

janela = tk.Tk()
janela.title("MensageBox")
janela.geometry("300x300")

#------------LABEL FRAME
tela = tk.LabelFrame(janela)
tela.pack(side=tk.BOTTOM)

lbl_nam = tk.Label(janela, text="Ensira seu nome aqui").pack()

#--------------TEXTO
lbl2 = tk.Label(janela, text="Ania")
lbl2.pack()

#------------INSERINDO IMAGEM
minhaimagem = tk.PhotoImage(file="ania2.png")
lbl = tk.Label(tela, image=minhaimagem)
lbl.image = minhaimagem
lbl.pack(side=tk.BOTTOM)

janela.mainloop()
