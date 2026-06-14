#Exercicio 1178 - Preenchimento de Vetor III

X = float(input())
N = [X]

Y = X 

for i in range(0,100,1): 
    print("N[%d] = %.4f" %(i, N[i]))
    Y = Y/2
    N.append(Y)
