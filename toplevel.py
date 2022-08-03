import tkinter as tk


def abrir_toplevel():
    janela_top = tk.Toplevel()
    janela_top.title("Janela Secundaria")
    janela_top.geometry("480x480")


janela_principal = tk.Tk()
janela_principal.title("Janela Principal")
janela_principal.geometry("480x480")
btn = tk.Button(janela_principal, text="Abrir", command=abrir_toplevel)
btn.pack()

janela_principal.mainloop()