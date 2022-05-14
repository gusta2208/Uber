import mysql.connector
import this

import conexaoBD
this.contador = 0
db_connection = conexaoBD.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def cadastrarMotorista(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento):
    try:
        sql = "insert into motorista (cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento) values ('{}','{}','{}','{}','{}','{}','{}')".format(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento)
        con.execute(sql) # prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!!")
    except Exception as erro:
        print(erro)

def consultarMotorista(CPFDigitado):#Consultar os dados do banco de dados
    try:
        sql = "select * from motorista where CPF = '{}'".format(CPFDigitado)
        con.execute(sql)

        for (CPF, nome, telefone, endereco, modelo, placa, dataDeNascimento) in con:
            dados = (CPF, nome, telefone, endereco, modelo, placa, dataDeNascimento)
            if (CPFDigitado == int(dados[0])):
                print(dados)
            else:
                print("Passei Aqui")
        print("\n")
    except Exception as erro:
        print(erro)

def atualizarNomeMotorista(CPF, nome ): #Atualizar os dados no banco de dados
    try:
        sql = "update motorista set nome = '{}' where CPF = '{}'".format(nome,CPF)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Nome Atualizado!!")
    except Exception as erro:
        print(erro)

def atualizarTelefoneMotorista(CPF, telefone):  # Atualizar os dados no banco de dados
    try:
        sql = "update motorista set telefone = '{}' where CPF = '{}'".format(telefone, CPF)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Telefone Atualizado!!")
    except Exception as erro:
        print(erro)

def atualizarEnderecoMotorista(CPF, endereco):  # Atualizar os dados no banco de dados
    try:
        sql = "update motorista set endereco = '{}' where CPF = '{}'".format(endereco, CPF)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Endereço Atualizado!!")
    except Exception as erro:
        print(erro)
def atualizarModeloMotorista(CPF, modelo):  # Atualizar os dados no banco de dados
    try:
        sql = "update motorista set modelo = '{}' where CPF = '{}'".format(modelo, CPF)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Modelo do veiculo Atualizado!!")
    except Exception as erro:
        print(erro)
def atualizarPlacaMotorista(CPF, placa):  # Atualizar os dados no banco de dados
    try:
        sql = "update motorista set placa = '{}' where CPF = '{}'".format(placa, CPF)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Placa do veiculo Atualizada!!")
    except Exception as erro:
        print(erro)
def atualizarDataMotorista(CPF, dataDeNascimento):  # Atualizar os dados no banco de dados
    try:
        sql = "update motorista set dataDeNascimento = '{}' where CPF = '{}'".format(dataDeNascimento, CPF)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Data De Nascimento Atualizada!!")
    except Exception as erro:
        print(erro)

def excluirMotorista(CPF):
    try:
        sql = "delete from motorista where CPF = '{}'".format(CPF)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletado!")
    except Exception as erro:
        print(erro)
def atualizarMotorista():
    print("   O Que Deseja Atualizar?   \n")

    print("1. Nome\n" +
          "2. Telefone\n"+
          "3. Endereço\n" +
          "4. Modelo do veiculo\n" +
          "5. Placa do veiculo\n" +
          "6. Data De Nascimento\n")
    this.opcao = int(input())

    if this.opcao == 1:
        print("Informe seu CPF: ")
        CPF = input()
        print("Informe o novo Nome: ")
        nome = input()
        atualizarNomeMotorista(CPF, nome)
    elif this.opcao == 2:
        print("Informe seu CPF: ")
        CPF = input()
        print("Informe o novo Telefone: ")
        telefone = input()
        atualizarTelefoneMotorista(CPF, telefone)
    elif this.opcao == 3:
        print("Informe seu CPF: ")
        CPF = input()
        print("Informe o novo Endereço: ")
        endereco = input()
        atualizarEnderecoMotorista(CPF, endereco)
    elif this.opcao == 4:
        print("Informe seu CPF: ")
        CPF = input()
        print("Informe o novo Modelo do veiculo: ")
        modelo = input()
        atualizarModeloMotorista(CPF, modelo)
    elif this.opcao == 5:
        print("Informe seu CPF: ")
        CPF = input()
        print("Informe a nova Placa: ")
        placa = input()
        atualizarPlacaMotorista(CPF, placa)
    elif this.opcao == 6:
        print("Informe seu CPF: ")
        CPF = input()
        print("Informe a nova Data De Nascimento ")
        dataDeNascimento = input()
        atualizarDataMotorista(CPF, dataDeNascimento)
def login():
    print("1. Consultar Cadastro \n" +
          "2. Alterar Dados\n" +
          "3. Deletar Conta\n" +
          "4. Disponível \n" +
          "5. Indisponível\n" +
          "0. Sair \n")
    this.opcaoLogin = int(input())
    if this.opcaoLogin == 1:
        print("Informe o CPF que deseja Consultar:")
        CPF = int(input())
        consultarMotorista(CPF)
    elif this.opcaoLogin == 2:
        atualizarMotorista()
    elif this.opcaoLogin == 3:
        print("Informe seu CPF: ")
        CPF = input()
        excluirMotorista(CPF)
    elif this.opcaoLogin == 4:
        print("Você está Indisponivel para receber corridas!")

    elif this.opcaoLogin == 5:
        print(" Agora você está disponível para receber novas corridas!")

    else:
        print("Obrigado!")
