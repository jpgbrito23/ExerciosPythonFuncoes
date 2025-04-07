#João Pedro Gomes de Brito
#2 Vetores aleatórios que se intercalam

import random 

def intercalam():
    vetor1 = []
    vetor2 = []
    vetor3 = []
    for i in range(10):
        vetor1.append(random.randrange(1,100))
        vetor2.append(random.randrange(1,100))
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])
    print (vetor1,vetor2,vetor3)


if __name__ == "__main__": 
    intercalam()
        