#! /usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
from tkfiledialog import asksaveasfilename, askopenfilename


# Começa a classe do editor:
class PyNotePad:
    # Aqui fica a função inicial:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("PyNotePad")  # Aqui é o digito

        # "inicia" a scroolbar
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)

        menubar = Menu(self.root)
        # Aqui criamos os menus:
        MENUarquivo = Menu(menubar)
        MENUarquivo.add_command(label="Salvar", command=self.salvar)
        MENUarquivo.add_command(label="Abrir", command=self.abrir)
        menubar.add_cascade(label="Arquivo", menu=MENUarquivo)

        MENUajuda = Menu(menubar)
        MENUajuda.add_command(label="Sobre", command=self.sobre)
        menubar.add_cascade(label="Ajuda", menu=MENUajuda)
        self.root.config(menu=menubar)

        # Aqui adicionamos a parte que fica o texto:
        self.text = Text(self.root)
        self.text.pack(expand=YES, fill=BOTH)

        # aqui configura o scrollbar
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        # Por Fim, a janela:
        self.root.mainloop()

    def salvar(self):  # Aqui é a função que salva o arquivo:

        fileName = asksaveasfilename()
        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def abrir(self):  # Aqui é a função que abre um arquivo

        fileName = askopenfilename()
        try:
            file = open(fileName, 'r')
            contents = file.read()

            self.text.delete(0.0, END)
            self.text.insert(0.0, contents)
        except:
            pass

    def sobre(self):  # uma pequena função "sobre" :D
        root = Tk()
        root.wm_title("Sobre")
        texto = ("PyNotePad: Versão 1.0")
        textONlabel = Label(root, text=texto)
        textONlabel.pack()


# inicia o programa:
PyNotePad()
