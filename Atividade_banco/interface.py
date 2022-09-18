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

def consultar():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        cursor.execute('SELECT * FROM clientes')
        consulta = cursor.fetchall()
  
        con.close()
        return consulta
    except Error as er:
        print(er)

def deletar(id):
    try:
        con = conectar_banco()
        cursor = con.cursor()
        
        cursor.execute(f'DELETE FROM clientes WHERE id="{id}"')
        
        con.commit()
        con.close()
    except Error as er:
        print(er)

def atualizar(id, nome, cpf):
    try:
        con = conectar_banco()
        cursor = con.cursor()
        
        cursor.execute(f'UPDATE clientes SET nome="{nome}", cpf="{cpf}" WHERE id="{id}"')
        
        con.commit()
        con.close()
    except Error as er:
        print(er)