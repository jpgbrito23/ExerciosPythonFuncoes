#João Pedro Gomes de Brito
#Criar vetor Inverso

import random

def VetorInverso():
    vetor = []
    for i in range(10):
        vetor.append(random.randrange(1,100))
    vetorInverso = vetor[::-1]
    print (vetor , vetorInverso)
    
if __name__ == "__main__":    
    VetorInverso()