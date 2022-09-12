
import sqlite3
from sqlite3 import Error

#con faz a conexão
def conectar_banco():
    try:
        con = None
        con = sqlite3.connect('banco_dados.db')
        return con
        print('Banco conectado')
    except Error as erro:
        print(erro)


def inserir(sql):
    con = conectar_banco()
    cursor = con.cursor()
    cursor.execute(sql)
    print('Registro inserido com sucesso')    
    con.commit()
    con.close()


sql_insert = 'INSERT INTO clientes VALUES("3","teste","12312312322")'

dele = 'DELETE FROM clientes WHERE id=1'

inserir()


#a = input('')
#inserir(a)
