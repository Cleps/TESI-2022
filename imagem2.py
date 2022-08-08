import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("MensageBox")
janela.geometry("300x300")

tela = tk.LabelFrame(janela)
tela.pack()

img = Image.open("ania1.jpeg")

minhaimagem = ImageTk.PhotoImage(img)

lbl2 = tk.Label(janela, text="Ania").pack()
lbl = tk.Label(tela, image=minhaimagem)
lbl.image = minhaimagem
lbl.pack()

janela.mainloop()
