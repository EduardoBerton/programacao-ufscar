#Exercício 1080 - Maior e Posição

N = 0
maior = 0
pos = 0 

for I in range (1, 101, 1):
    N = int(input())
    if (N > maior):
        maior = N
        pos = I
print(maior)
print(pos)



