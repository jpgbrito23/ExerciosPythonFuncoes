#João Pedro Gomes de Brito
#Menu dos exercícios

import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import ex8
import ex9
import ex10
import ex11
import ex12

def Menu():
    continuar= 's'
    while continuar == 's':
        opcao = int(input("Digite um número de 1 a 12 para opções de exercicios ou 0 para sair: "))
        if 0<= opcao <= 12 :
            if opcao == 1:
                 ex1.ParImpar()
            elif opcao == 2:
                 ex2.NumMult6()
            elif opcao == 3:
                 ex3.VetorInverso()
            elif opcao == 4:
                 ex4.intercalam()
            elif opcao == 5:
                 ex5.SomaVetores()
            elif opcao == 6:
                 ex6.MatrizSequencial()
            elif opcao == 7:
                 ex7.Maiusculo()
            elif opcao == 8:
                 ex8.Frase()
            elif opcao == 9:
                 ex9.RetirarCaracter()
            elif opcao == 10:
                 ex10.ParouImpar()
            elif opcao == 11:
                 ex11.Dados()
            elif opcao == 12:
                 ex12.AnoBissexto()
            else:
                break
        else:
            print("Digite um número dentro os possiveis!")
        continuar = input("Deseja continuar: (s/n) ").lower().strip()
    
Menu()