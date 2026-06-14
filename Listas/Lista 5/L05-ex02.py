#Exercício 1177 - Preenchimento de vetores II
# T - Número arbitrário
# N - Lista com 1000 elementos
# i - Contador para as posições da lista
# x - elementos da lista, dependem de T

T = 0
while T < 2 or T > 50:
    T = int(input())

N = []
i = 0

while len(N) < 10: 

    for x in range(0,T,1):
        N.append(x)
        print(f"N[{i}] = {N[i]}")
        i += 1

        if len(N) == 10: 
            break
    


