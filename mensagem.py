import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("MensageBox")
janela.geometry("300x300")
def info():
    messagebox.showinfo("Exemplo Info", "Aqui vai a mensagem")

btn1 = tk.Button(janela, text="Informação", command=info)
btn1.pack()

def aviso():
    messagebox.showwarning("Aviso", "Você foi avisado!")

btn2 = tk.Button(janela, text="Aviso", command=aviso)
btn2.pack()

def pergunte():
    teste = messagebox.askyesnocancel("Pergunta", "Continuar?")
    print(teste)

btn3 = tk.Button(janela, text='Pergunte', command=pergunte)
btn3.pack()

janela.mainloop()