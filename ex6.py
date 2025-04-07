#João Pedro Gomes de Brito
#Matriz sequencial
 
def MatrizSequencial():
    for i in range(1,6):
        for j in range(1,6):
            print(f"{i * 10 + j}",end=" ")
        print()
        
if __name__ == "__main__":
    MatrizSequencial()