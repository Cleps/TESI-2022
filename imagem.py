import tkinter as tk

janela = tk.Tk()
janela.title("MensageBox")
janela.geometry("300x300")

#------------LABEL FRAME
tela = tk.LabelFrame(janela)
tela.pack()

#--------------TEXTO
lbl2 = tk.Label(janela, text="Ania")
lbl2.pack()

#------------INSERINDO IMAGEM
minhaimagem = tk.PhotoImage(file="ania2.png")
lbl = tk.Label(tela, image=minhaimagem)
lbl.image = minhaimagem
lbl.pack()

janela.mainloop()
