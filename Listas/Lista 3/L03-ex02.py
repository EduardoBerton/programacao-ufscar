#Exercício 1066 - Pares, ímpares, Positivos e Negativos

i = 0 
neg = 0
pos = 0
par = 0
impar = 0

while (i < 5):
    N = int(input().split())

    if (N < 0):
        neg += 1
    elif (N > 0):
        pos += 1
    
    if (N%2 == 0):
        par += 1
    elif (N%2 != 0):
        impar += 1

    i += 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")


    