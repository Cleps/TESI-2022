import tkinter as tk

app = tk.Tk()
app.title("Exemplo LabelFrame")
app.geometry("320x320")

lfr1 = tk.LabelFrame(app, text="Alinhamento")
lfr1.pack()

v=tk.IntVar()
b=tk.IntVar()
n=tk.IntVar()

btn1 = tk.Radiobutton(lfr1, text="LEFT", variable=v)
btn1.pack(side=tk.LEFT)
btn2 = tk.Radiobutton(lfr1, text="CENTER", variable=b)
btn2.pack(side=tk.LEFT)
btn3 = tk.Radiobutton(lfr1, text="RIGHT", variable=n)
btn3.pack(side=tk.LEFT)

app.mainloop()
