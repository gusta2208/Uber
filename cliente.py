import this
import time, conexaoCliente
import operacoes, avalicao

this.localidade = 0
this.opcao = 0
this.opcaoMotorista = 0
this.opcaoAvaliacao = 0
this.comentario = 0
this.opcaoCadastro = 0
this.opcaoAdmin = 0
this.opcaoCliente = 0
this.opcaoLogin = 0
this.opcaoBemVindo = 0



def bemVindo():
    print("    \n Bem vindo a Uber!  \n\n"      +
          "1.Iniciar Corrida\n"                +
          '2.Consultar Dados\n'                 +
          '3.Atualizar nome\n'                  +
          '4.Atualizar telefone\n'              +
          '5.Atualizar endereço\n'              +
          '6.Excluir conta\n'                   +
          '0.Sair')
    this.opcaoBemVindo = int(input())
    if this.opcaoBemVindo == 1:
        mostrar()

    elif this.opcaoBemVindo == 2:
        conexaoCliente.selecionar()

    elif this.opcaoBemVindo == 3:
        print('Informe o código: ')
        codigo = input()
        print('Informe o novo nome: ')
        nome = input()
        # Uso do método
        conexaoCliente.atualizarNome(codigo, nome)

    elif this.opcaoBemVindo == 4:
        print('Informe o código: ')
        codigo = input()
        print('Informe o novo telefone: ')
        telefone = input()
        # Uso do método
        conexaoCliente.atualizarTelefone(codigo, telefone)

    elif this.opcaoBemVindo == 5:
        print('Informe o código: ')
        codigo = input()
        print('Informe o novo endereço: ')
        endereco = input()
        # Uso do método
        conexaoCliente.atualizarEndereco(codigo, endereco)

    elif this.opcaoBemVindo == 6:
        print('Infome o codigo: ')
        codigo = input()
        conexaoCliente.excluir(codigo)

    elif this.opcaoBemVindo == 0:
        print('Obrigado!')




def cadastroCliente():
    print('Informe seu CPF: ')
    cpf = input()
    print('Informe seu nome: ')
    nome = input()
    print('Informe seu telefone: ')
    telefone = input()
    print('Informe seu endereço ')
    endereco = input()
    print('Informe a sua data de nascimento: ')
    dataNascimento = input()
    # Utilizar o método cadastrar
    conexaoCliente.inserir(cpf, nome, telefone, endereco, dataNascimento)
    print('Cadastrado com sucesso!!!\n\n')

def mostrarMenu():
    print("Onde você se encontra? \n" +
            "1. Santo André\n"        +
            "2. São Bernardo\n"       +
            "3. São Caetano\n"     +
            "4. Mauá\n" +
            "5. Diadema\n" +
            "6. Guarulhos\n"
            "7. Embu das Artes\n" +
            "8. Campinas\n" +
            "9. Boituva\n" +
            "10. Barueri\n")
    this.opcao = int(input())

def operacao():
    mostrarMenu()
    if this.opcao == 1:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Julio Souza(★★★★★). 10km de distancia" +
              "\n2. Antonio Farias(★★★★★) á 2km de voçê " +
              "\n3. Gustavo Almeida(★★★★★) á 2km de voçê" +
              "\n4. Gabriela Silva(★★★★★) á 2km de voçê" +
              "\n5. Evandra Soares(★★★★★) á 2km de voçê")
        this.opcaoMotorista = int(input())
        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()

    elif this.opcao == 2:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
                "\n1. Adagoberto Farias (★★) á 1,2km de você" +
                "\n2. Guilherme Botelho (★) á 4,6km de você" +
                "\n3. Andreia Silva (★★★★) á 3,2km de você" +
                "\n4. Gabriel Moraes (★★★) á 4,2km de você" +
                "\n5. Pedro Guilherme (★★★★★) á 4,9km de você")
        this.opcaoMotorista = int(input())
        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()

    elif this.opcao == 3:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Valentina Pereira (★★★★★) á 2,1km de você" +
              "\n2. Sophia Abravanel (★★★★) á 2,6km de você" +
              "\n3. Aline Gobertina (★★★) á 3,2km de você" +
              "\n4. Pedro Miguel (★★) á 2,2km de você" +
              "\n5. Joaquim Calembrari(★) á 1,4km de você")
        this.opcaoMotorista = int(input())
        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()

    elif this.opcao == 4:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Gabriela Alves (★) á 2,9km de você" +
              "\n2. Gustavo Medina (★★) á 1,6km de você" +
              "\n3. Felipe Coutinho (★★★) á 3,1km de você" +
              "\n4. André Adogoberto (★★★★) á 2,3km de você" +
              "\n5. Jucelina Alves (★★★★★) á 4,1km de você")
        this.opcaoMotorista = int(input())
        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()

    elif this.opcao == 5:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Diego Batagim (★★★★) 1,9á km de você" +
              "\n2. Rafael Pereira (★★★) 3á km de você" +
              "\n3. Rafael Melo (★★★★★) á 2,3km de você" +
              "\n4. Vinicius Morais (★★) á 7,8km de você" +
              "\n5. Allan Sobral (★) á 1km de você")
        this.opcaoMotorista = int(input())
        avalicao.avaliar()

    elif this.opcao == 6:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Gustavo Rafael(★★★★). 10km de distancia" +
              "\n2. Antonio Silva(★★★) á 2km de voçê" +
              "\n3. Vinicius Eduardo(★★★★) á 6km de voçê" +
              "\n4. Mateus pereira(★★★★) á 12km de voçê" +
              "\n5. Cristiano Soares(★★★★★) á 4km de voçê")
        this.opcaoMotorista = int(input())
        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()

    elif this.opcao == 7:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Guilherme Souza(★★) 11km de distancia" +
              "\n2. Aline Farias(★★★★★) á 4km de voçê" +
              "\n3. Pedro Almeida(★★★★) á 5km de voçê" +
              "\n4. Gabriel Silva(★★★★) á 1km de voçê" +
              "\n5. Diego edmundo(★★★★★) á 5km de voçê")
        this.opcaoMotorista = int(input())
        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()
    elif this.opcao == 8:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Alan Souza(★) 8km de distancia" +
              "\n2. Pedro Farias(★★★★) á 2km de voçê" +
              "\n3. Jean Lucas(★★★) á 2km de voçê" +
              "\n4. Messi Silva(★★) á 3km de voçê" +
              "\n5. Neymar Soares(★★★★★) á 4km de voçê")
        this.opcaoMotorista = int(input())
        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()


    elif this.opcao == 9:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Lionel Antonio(★) 3km de distancia" +
              "\n2. Pablo (★★★★) á 2km de voçê" +
              "\n3. Gustavo Almeida(★★★★) á 4km de voçê" +
              "\n4. Gabriela Silva(★★★★★) á 4km de voçê" +
              "\n5. Evandra Soares(★★★★) á 9km de voçê")
        this.opcaoMotorista = int(input())
        avalicao.avaliar()

    elif this.opcao == 10:
        print("Motoristas Na Sua Localidade, escolha o melhor para você.\n")

        print("Motoristas Disponiveis: \n" +
              "\n1. Julio Souza(★) 1km de distancia" +
              "\n2. Antonio Farias(★★★★) á 3km de voçê" +
              "\n3. Gustavo Almeida(★★★★★) á 2km de voçê" +
              "\n4. Gabriela Silva(★★★) á 4km de voçê" +
              "\n5. Evandra Soares(★★) á 6km de voçê")
        this.opcaoMotorista = int(input())

        if this.opcaoMotorista == 1 or 5:
            avalicao.avaliar()
def mostrar():
    operacao()
def mostrar2():
    cadastroCliente()