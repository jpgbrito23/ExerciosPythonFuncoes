#João Pedro Gomes de Brito
#Vetor de 15 posições e leia os números dizendo se são pares ou ímpares
import random 

def ParImpar():
    vetor = []
    for i in range(15):
        vetor.append(random.randrange(1,100))

    for j in range(15):
        if vetor[j] % 2 == 0:
            print(f"O Número {j+1} é par. {vetor[j]}")
        else:
            print(f"O Número {j+1} é ímpar. {vetor[j]}")
            
            
if __name__ == "__main__":
    ParImpar()