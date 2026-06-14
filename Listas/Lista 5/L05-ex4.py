#Exercicio 1179 - Prenchimento de Vetores IV

par = []
impar = []

for i in range(15):  #Trocar pra 15
    N = int(input())

    if N%2 == 0: 
        par.append(N)

        if len(par) == 5: 
            for num in range(5): 
                print(f"par[{num}] = {par[num]}")
            par = []
    
    else: 
        impar.append(N)

        if len(impar) == 5: 
            for num in range(5): 
                print(f"impar[{num}] = {impar[num]}")
            impar = []

for num in range(len(impar)): 
    print(f"impar[{num}] = {impar[num]}")
for num in range(len(par)):
    print(f"par[{num}] = {par[num]}")

        

    



    






