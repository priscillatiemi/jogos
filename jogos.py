import forca
import jogo_adivinhacao_random


def escolher_jogo():
    print("**********************************")
    print("*******Escolha o seu jogo!********")
    print("**********************************")

    print("(1)Forca  (2)Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if (jogo == 1):
        print("Jogando Forca.......")
        forca.jogo_forca()
    elif (jogo == 2):
        print("Jogando adivinhação......")
        jogo_adivinhacao_random.jogo_adivinhacao()

if(__name__ == "__main__"):
    escolher_jogo()
