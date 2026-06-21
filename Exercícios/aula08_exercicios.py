n = int(input("qtd: "))
lista = []

for i in range(1,n+1,1):

    lista.append(int(input()))
    
print(lista)

maior = 0
pos = 0

for j in lista: 
    if (j > maior): 
        maior = j
        pos = pos
    pos += 1

print(maior)
print(pos)












