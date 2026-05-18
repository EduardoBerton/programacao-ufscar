#Exercício 1060 - Números Positivos

NUM = 0
POS = 0

for I in range(1,7,1):
    NUM = float(input())
    if (NUM > 0):
        POS += 1

print(f"{POS} valores positivos")
    