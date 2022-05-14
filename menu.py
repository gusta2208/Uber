import operacoes, this, cliente
this.opcao = -1

def menuLogin():
    print("    \n Bem vindo a Uber!  \n\n" +

          "1.Login\n"
          "2.Cadastro \n\n\n" +
          '3.Sou Motorista\n')
    this.opcaoGeral = int(input())

    if this.opcaoGeral == 1:
        cliente.bemVindo()
    elif this.opcaoGeral == 2:
        cliente.cadastroCliente()
        cliente.bemVindo()
    else:
        menuMotorista()

def menuMotorista():
    print("Bem vindo Motorista!!! \n")
    print("Escolha uma das opções abaixo: \n\n" +
          "1. Login\n" +
          "2. Cadastre-se\n" +
          "0. Sair")
    this.opcao = int(input())
    if this.opcao == 1:
        operacoes.login()
    elif this.opcao == 2:
        print("Informe seu CPF: ")
        cpf = input()
        print("Informe seu Nome: ")
        nome = input()
        print("Informe seu Telefone: ")
        telefone = input()
        print("Informe o seu Endereço: ")
        endereco = input()
        print("Informe o Modelo do Veiculo")
        modelo = input()
        print("Informe A Placa do Veiculo")
        placa = input()
        print("Informe Sua Data de nascimento: ")
        dataDeNascimento = input()

        operacoes.cadastrarMotorista(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento)
    elif this.opcao == 1:
        print("Obrigado!!")
def operacao():
    while (this.opcao != 0):
        menuMotorista()
        if this.opcao == 1:
            operacoes.login()
        if this.opcao == 2:
            print("Informe seu CPF: ")
            cpf = input()
            print("Informe seu Nome: ")
            nome = input()
            print("Informe seu Telefone: ")
            telefone = input()
            print("Informe o seu Endereço: ")
            endereco = input()
            print("Informe o Modelo do Veiculo")
            modelo = input()
            print("Informe A Placa do Veiculo")
            placa = input()
            print("Informe Sua Data de nascimento: ")
            dataDeNascimento = input()

            #Ultilizar o método cadastrar
            operacoes.cadastrarMotorista(cpf, nome, telefone, endereco, modelo, placa, dataDeNascimento)
        elif this.opcao == 3:
            print("Informe o CPF que deseja Consultar:")
            CPF = int(input())
            operacoes.consultarMotorista(CPF)
        elif this.opcao == 4:
            operacoes.atualizar()
        elif this.opcao == 5:
            print("Informe seu CPF: ")
            CPF = input()
            operacoes.excluirMotorista(CPF)
        elif this.opcao == 0:
            print("Obrigado!")