#João Pedro Gomes de Brito
#Quantida de carcter na string


def Frase():
    string = str(input("Digite uma frase: "))
    caracter = str(input("Digite um caracter: ")).strip().lower()
    if len(caracter) != 1:
        print("Digite apenas 1 caracter!")
    else:
        print(f"O caracter se repete {string.count(caracter)} vezes!")
     
if __name__ == "__main__":
    Frase()
    
    
