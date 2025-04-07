#João Pedro Gomes de brito
#NVetor de 30 posições números Multiplos de 6

import random

def NumMult6():
    vetor = []
    for i in range(30):
        vetor.append(random.randrange(1,100))
        
    for j in range(30):
        if vetor[j] % 6 == 0:
            print(f"O número {j+1} é múltiplo de 6. {vetor[j]}")
        else:
            print(f"O número {j+1} não é múltiplo de 6. {vetor[j]}")
            
            
if __name__ == "__main__":         
    NumMult6()