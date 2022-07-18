import tkinter as tk

janela = tk.Tk()
janela.geometry('330x130')

lbl1 = tk.Label(janela, text='LEFT', bg='red')
lbl1.pack(fill=tk.BOTH, expand=True)

lbl2 = tk.Label(janela, text='RIGHT', bg='blue')
lbl2.pack(anchor=tk.E)

janela.mainloop()
