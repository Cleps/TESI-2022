import tkinter as tk

app = tk.Tk()
app.title("Exemplo com frames")
app.geometry("480x320")


frm1 = tk.LabelFrame(app,text="Botões")
frm1.pack()
frm2 = tk.LabelFrame(app, text="-----Outros botões-----")
frm2.pack()


btn1 = tk.Button(frm1, text="Adicionar")
btn1.pack(side=tk.LEFT)
btn2 = tk.Button(frm1, text="Editar")
btn2.pack(side=tk.LEFT)
btn3 = tk.Button(frm1, text="Remover")
btn3.pack(side=tk.LEFT)
btn4 = tk.Button(frm2, text="Salvar")
btn4.pack(side=tk.BOTTOM)
btn5 = tk.Button(frm2, text="Fechar")
btn5.pack(side=tk.BOTTOM)
btn6 = tk.Button(frm2, text="Listar")
btn6.pack(side=tk.BOTTOM)

app.mainloop()