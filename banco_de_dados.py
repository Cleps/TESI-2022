
import sqlite3
from sqlite3 import Error
from unittest import result

#con faz a conexão
def conectar_banco():
    try:
        con = None
        con = sqlite3.connect('banco.db')
        return con
        print('Banco conectado')
    except Error as erro:
        print(erro)


def inserir(sql):
    try:
        con = conectar_banco()
        cursor = con.cursor()
        cursor.execute(sql)
        print('Registro inserido com sucesso')    
        con.commit()
        con.close()
    except Error as er:
        print(er)

def remover(sql):
    try:
        con = conectar_banco()
        cursor = con.cursor()
        cursor.execute(sql)
        print('REMOVIDO!')
        con.commit()
        con.close()
    except Error as er:
        print(er)

def consultar(sql):
    try:
        con = conectar_banco()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado

    except Error as er:
        print(er)

sql_insert = 'INSERT INTO cliente VALUES("3","teste","12312312322")'
sql = 'CREATE TABLE if not exists cliente(id INTEGER, nome TEXT, telefone TEXT)'
dele = 'DELETE FROM clientes WHERE id=1'
al_nome = 'UPDATE cliente SET nome="BILL" where id="3"'
al_id = 'UPDATE cliente SET id="1" WHERE id="3"'
consulta = 'SELECT * FROM cliente'

#inserir(al_id)
print(consultar(consulta))


#a = input('')
#inserir(a)
