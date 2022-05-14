import mysql.connector
import this

import conexaoBD
this.contador = 0
db_connection = conexaoBD.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


def inserir(cpf, nome, telefone, endereco, dataNascimento):
    try:
        sql = "insert into cliente(codigo, cpf, nome, telefone, endereco, dataNascimento) values('','{}','{}','{}','{}','{}')".format(
            cpf, nome, telefone, endereco, dataNascimento)
        con.execute(sql)  # Prepara o comando para ser executado
        db_connection.commit()  # Executa o comando no banco de dados
        print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)


# Consultar os dados do BD
def selecionar():
    try:
        sql = "select * from cliente"
        con.execute(sql)

        for (codigo, cpf, nome, telefone, endereco, dataNascimento) in con:
            print(codigo, nome, telefone, endereco, dataNascimento)
        print('\n')
    except Exception as erro:
        print(erro)


# Atualizar dados no banco de dados
def atualizarNome(codigo, nome):
    try:
        sql = f"update cliente set nome = '{nome}' where codigo = '{codigo}';"
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)


def atualizarEndereco(codigo, endereco):
    try:
        sql = f"update cliente set endereco = '{endereco}' where codigo = '{codigo}';"
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)


def atualizarTelefone(codigo, telefone):
    try:
        sql = f"update cliente set telefone = '{telefone}' where codigo = '{codigo}';"
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)


def atualizarData(codigo, dataNascimento):
    try:
        dataNascimento = transformarData(dataNascimento)
        sql = f"update cliente set dataNascimento = '{dataNascimento}' where codigo = '{codigo}';"
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)


def excluir(codigo):
    try:
        sql = "delete from cliente where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletar!")
    except Exception as erro:
        print(erro)


def transformarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano, mes, dia)