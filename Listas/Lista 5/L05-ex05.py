#Exercício  1180 - Menor e Posição
# menor = min(X) - Dá o menor
# X.index(menor) - Dá a posição

N = int(input())
X = list(map(int, input().split()))

menor = X[0]
pos = 0
posf = 0

for valor in X:
    if valor < menor: 
        menor = valor
        posf = pos
    pos += 1

print(f"Menor valor: {menor}")    
print(f"Posicao: {posf}") 