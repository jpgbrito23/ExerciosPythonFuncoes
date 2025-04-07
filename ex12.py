#João Pedro gomes de Brito
#Ano bissexto

def AnoBissexto():
    ano = int(input("Digite um ano: "))
    if ano % 4 == 0 and ano % 100 != 0:
        print ("O ano é bissexto")
    else:
        print ("O ano não é bissexto")
    
if __name__ == "__main__":
    AnoBissexto()