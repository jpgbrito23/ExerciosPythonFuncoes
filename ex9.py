#João Pedro Gomes de Brito
#Retirar Caracter de uma frase

def RetirarCaracter():
    frase = str(input("Digite uma frase: "))
    caracter = str(input("Digite um caracter: ")).strip().lower()
    if len(caracter) != 1:
        print("Digite apenas 1 caracter!")
    else:
        print(frase.replace(caracter, ''))


if __name__ == "__main__":
    RetirarCaracter()