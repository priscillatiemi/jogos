print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("*********************************")
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = int(input("Digite o seu numero: "))

    print("Você digitou", chute)

    acertou = chute == numero_secreto

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (acertou):
        print("Parabéns, você acertou o número secreto ", numero_secreto)
    else:
        if(maior):
            print("Você errou! Seu chute foi maior do que o numero secreto!")
        elif(menor):
            print("Você errou! Seu chute foi menor do que o numero secreto!")
    rodada = rodada + 1

print("**********************************")
print("Fim do jogo")
print("**********************************")
