import sqlite3
from sqlite3 import Error

'''
INTERFACE COM FUNÇÕES UTEIS DO BANCO DE DADOS, CRIANDO UM BANCO DE CLIENTES COM NOME E CPF
conectar_banco = cria um 'banco.db' caso não exista
create_table_banco = cria uma tabela de clientes caso não exista
inserir_banco(nome, cpf) = passe o nome e o cpf de um cliente para inserir no bd
consultar = retorna todos os dados do bd
deletar = deleta um cliente pela id do mesmo
atualizar(id, nome, cpf) = passe um novo nome e novo cpf e a id do cliente q deseja atualizar os dados
'''


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

        cursor.execute(
            'CREATE TABLE if not exists clientes (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, cpf TEXT NOT NULL)')

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

        # print('Registro inserido com sucesso')
        con.commit()
        con.close()
    except Error as er:
        print(er)


def executar(sql):
    try:
        con = conectar_banco()
        cursor = con.cursor()

        cursor.execute(sql)
        consulta = cursor.fetchall()

        con.close()
        return consulta
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

def consultar_contas():
    try:
        con = conectar_banco()
        cursor = con.cursor()

        #cursor.execute('SELECT * FROM conta NATURAL JOIN clientes ')

        cursor.execute('''SELECT c.id, c.numero,  cli.nome, c.saldo  
        FROM conta c, clientes cli 
        WHERE cli.id = c.id_cliente ''')
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