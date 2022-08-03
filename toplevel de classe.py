import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela_principal = master
        self.janela_principal.title("Janela Principal")
        self.janela_principal.geometry("480x480")
        self.btn = tk.Button(master, text="Abrir", command=self.abrir_toplevel)
        self.btn.pack()

    def abrir_toplevel(self):
        self.janela_principal.iconify()
        self.janela_top = tk.Toplevel(bg="darkcyan")
        self.janela_top.title("Janela Secundaria")
        self.janela_top.geometry("480x480")
        self.btn2 = tk.Button(self.janela_top, text="Fechar", command=self.fechar_toplevel).pack()
        self.janela_top.grab_set()


    def fechar_toplevel(self):
        self.janela_top.destroy()
        self.janela_principal.deiconify()

app = tk.Tk()
Tela(app)
app.mainloop()

janela_principal.mainloop()