import random

def jogo_adivinhacao():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1)Facil  (2)Médio  (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print(numero_secreto)
    for rodada in range(1, total_de_tentativas + 1):
        print("*********************************")
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um numero entre 1 e 100: "))

        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print("Parabéns, você acertou o número secreto: ", numero_secreto)
            print("Você fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior do que o numero secreto!")
            elif (menor):
                print("Você errou! Seu chute foi menor do que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("**********************************")
    print("Fim do jogo")
    print("**********************************")

if(__name__ == "__main__"):
    jogo_adivinhacao()