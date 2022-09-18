import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from tkinter.scrolledtext import ScrolledText

janela = tk.Tk()
janela.title("Evento com arquivos")
janela.geometry("300x300")

def mostrar_arquivo():
    nome_arquivo = fd.askopenfilename()
    ms.showinfo("Aviso", f"{nome_arquivo}")

#---------------------------ABRINDO E LENDO UM ARQUIVO
def carregar_arquivo():
    tipos = (('Texto',"*.txt"), ("Python", "*.py"))
    arquivo = fd.askopenfile(initialdir="/home/clecio.silva/Documentos/", filetypes=tipos)

    with open(arquivo.name, "r") as arq:
        for linha in arq:
            sct.insert(tk.END, linha)
            #print(linha, end='')

def salvar_arquivo():
    arquivo = fd.asksaveasfile()
    with open(arquivo.name, 'w') as arq:
        arq.write(sct.get("1.0", tk.END))


btn1 = tk.Button(janela, text="Mostrar arquivo", command=mostrar_arquivo).pack()
btn2 = tk.Button(janela, text="Carregar arquivo", command=carregar_arquivo).pack()
sct = ScrolledText(janela, height=10)
sct.pack()
btn3 = tk.Button(janela, text="Salvar arquivo", command=salvar_arquivo).pack()





janela.mainloop()