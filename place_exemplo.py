import tkinter as tk

janela = tk.Tk()
janela.geometry('330x130')

lbl1 = tk.Label(janela, text='x=40, y=10', bg='yellow')
lbl1.place(x=40,y=10,anchor='center')

lbl2 = tk.Label(janela, text='x=50, y=40', bg='blue')
lbl2.place(x=50,y=40, anchor='center')

lbl3 = tk.Label(janela, text='x=70, y=80', bg='red')
lbl3.place(x=70,y=80, anchor='center')

lbl4 = tk.Label(janela, text='relx=0.5, rely=0.5', bg='orange')
lbl4.place(relx=0.5,rely=0.5, anchor='center')


janela.mainloop()
