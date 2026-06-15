#Exercício 1175 - Troca em Vetor I

N = []
i = 0 

while i < 20:  
    num = int(input())
    N.append(num)
    i += 1

N = N[::-1] 
i = 0

for number in N: 
    print(f"N[{i}] = {N[i]}")
    i += 1
    




    
