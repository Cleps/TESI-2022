import tkinter as tk

janela = tk.Tk()
janela.geometry('330x130')

lbl1 = tk.Label(janela, text='Usuario')
lbl1.grid(row=0, column=0)

ent1 = tk.Entry(janela, width=20)
ent1.grid(row=0,column=1)

lbl2 = tk.Label(janela, text='Senha')

ent2 = tk.Entry(janela, width=20)
lbl2.grid(row=1,column=0)
ent2.grid(row=1,column=1)

btn = tk.Button(janela, text='Logar')
btn.grid(row=2,column=1)

janela.mainloop()
