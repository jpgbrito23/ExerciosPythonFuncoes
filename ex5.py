#João Pedro Gomes de Brito
#Soma de vetores de 5 posições

import random

def SomaVetores():
    vetor1 = []
    vetor2 = []
    vetor3 = []
    vetor4 = []
    operadores ="+*-/"
    for i in range(5):
        vetor1.append(random.randrange(1,10))
        vetor2.append(random.randrange(1,10))
        vetor3.append(random.choice(operadores))
        if vetor3[i] == '+':
            vetor4.append(vetor1[i] + vetor2[i])
        elif vetor3[i] == '-':
            vetor4.append(vetor1[i] - vetor2[i])
        elif vetor3[i] == '*':
            vetor4.append(vetor1[i] * vetor2[i])
        else:
            vetor4.append(vetor1[i] / vetor2[i])    
    print(vetor1)
    print(vetor3)
    print(vetor2)
    print(vetor4)
    
    
if __name__ == "__main__":
    SomaVetores()
        