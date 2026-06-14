
lista = []

while (len(lista) <= 10): 
    a = int(input())
    lista.append(a)

    if (a == 0): 
        del(lista[-1])
        print("FIM")
        break

    elif (len(lista) > 10):
        print("LIMITE")

media = 0
for i in lista: 
    media += i
media /= len(lista)

print("LISTA: ", lista)
print("MED: ", media)

