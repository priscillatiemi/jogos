print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
    print("*********************************")
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = int(input("Digite um numero entre 1 e 100: "))

    print("Você digitou", chute)

    if(chute < 1 or chute > 100):
        print("Digite um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (acertou):
        print("Parabéns, você acertou o número secreto ", numero_secreto)
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior do que o numero secreto!")
        elif(menor):
            print("Você errou! Seu chute foi menor do que o numero secreto!")


print("**********************************")
print("Fim do jogo")
print("**********************************")
