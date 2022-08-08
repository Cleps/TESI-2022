import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela_principal = master
        self.janela_principal.title("Janela Principal")
        self.janela_principal.geometry("380x380")
        a = "OLA"
        self.tela = tk.LabelFrame(self.janela_principal, text="aa").pack()
        self.lbl = tk.Label(self.tela, text=a, bg="blue", width=40, height=2).pack()


    def abrir_toplevel(self):
        pass





app = tk.Tk()
Tela(app)
app.mainloop()

janela_principal.mainloop()