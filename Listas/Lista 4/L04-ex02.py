#Exercício 1067 - Números Ímpares

X = int(input())

for I in range(1,X,1):
    if (I%2 != 0): 
        print(I)
if (X%2 != 0): 
    print(X)