import sqlite3
from sqlite3 import Error

def conectar_banco():
    try:
        con = None
        con = sqlite3.connect('banco.db')
        return con
    except Error as erro:
        print(erro)

def create_table_banco():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        cursor.execute('CREATE TABLE if not exists clientes (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, cpf TEXT NOT NULL)')

        print('Banco conectado!')    
        con.commit()
        con.close()
    except Error as er:
        print(er)

def inserir_banco(nome, cpf):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        cursor.execute(f'INSERT INTO clientes (nome, cpf) VALUES("{nome}", "{cpf}")')

        #print('Registro inserido com sucesso')    
        con.commit()
        con.close()
    except Error as er:
        print(er)