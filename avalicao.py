import this, time

this.num1 = 0
this.num2 = 0
this.num3 = 0
this.media = 0

def avaliar():

    # Avaliação do Motorista
    print("Informe para onde você deseja ir: ")

    this.localidade = str(input())
    print("Motorista a Caminho, aguarde no local!")
    time.sleep(3)
    print("Motorista no local solicitado!")
    time.sleep(3)
    print("Você Chegou ao seu Destino!!")

    print("\nAvalie o Motorista:" +
          "\n1. ★" +
          "\n2. ★★" +
          "\n3. ★★★" +
          "\n4. ★★★★" +
          "\n5. ★★★★★")
    this.opcaoAvaliacao = int(input())
    print("\nAvalie a Corrida:" +
          "\n1. ★" +
          "\n2. ★★" +
          "\n3. ★★★" +
          "\n4. ★★★★" +
          "\n5. ★★★★★")
    this.opcaoAvaliacao2 = int(input())
    print("\nAvalie o Estado do carro:" +
          "\n1. ★" +
          "\n2. ★★" +
          "\n3. ★★★" +
          "\n4. ★★★★" +
          "\n5. ★★★★★")
    this.opcaoAvaliacao3 = int(input())
    #Avaliação Motorista
    this.num1 = this.opcaoAvaliacao
    # Avaliação Corrida
    this.num2 = this.opcaoAvaliacao2
    # Avaliação Estado do carro
    this.num3 = this.opcaoAvaliacao3
    this.media = (this.num1 + this.num2 + this.num3) / 3

    print("Deixe seu comentário sobre a corrida")
    this.comentario = str(input())
    print("Obrigado pelo FeedBack!!")
    print("Média de Avaliação do Motorista: " + str(this.media))