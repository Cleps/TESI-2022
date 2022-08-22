from curses import BUTTON1_CLICKED, KEY_A1
from platform import java_ver
import tkinter as tk

janela = tk.Tk()
janela.geometry("300x250")

def left(event):
    btn2['bg'] = 'pink'
def right(event):
    btn2['bg'] = 'black'
    btn2['fg'] = '#fcfcfc'

btn1 = tk.Button(janela, text="Alterar cor")
btn1.pack()
btn2 = tk.Button(janela, text="Alteração")
btn2.pack()

#   btn.bind('<>', evento)
btn1.bind('<Button-1>', left)
btn1.bind('<Button-3>', right)

btn1.bind('<Enter>', left, add='+')
btn1.bind('<Leave>', right, add='+')

janela.mainloop()