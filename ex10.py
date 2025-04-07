#João Pedro Gomes de Brito
#Jogo par ou ímpar
import random

def ParouImpar():
    selecao = str(input("Par ou impar: ")).strip().lower()
    NumUsr = input("Digite número de 0 a 5: ").strip()
    NumMaq = random.randint(0,5)
    if len(NumUsr) != 1:
        print("Digite apenas 1 número")
    else:
        NumUsr = int(NumUsr)
        soma = NumUsr + NumMaq
        if soma % 2 == 0:
            if selecao == 'par':
                print("O usuário ganhou")
            else:
                print("A máquina ganhou")
        else:
            if selecao == 'impar':
                print ("O usuário ganhou")
            else:
                print ("A máquina ganhou")  
              

if __name__ == "__main__":
    ParouImpar()