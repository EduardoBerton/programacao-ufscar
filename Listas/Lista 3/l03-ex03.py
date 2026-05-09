#Exercício 1071 - Soma de Ímpares Consecutivos I

X = int(input())
Y = int(input())

 
IMPAR = 0
if (X > Y): 
    I = Y + 1
    while (Y < I < X): 
        if (I%2 != 0): 
            IMPAR += I
        I += 1
    print(IMPAR)  

elif (X < Y): 
    I = X + 1
    while (X < I < Y): 
        if (I%2 != 0): 
            IMPAR += I
        I += 1
    print(IMPAR)  

else: 
    print(IMPAR)   

         



