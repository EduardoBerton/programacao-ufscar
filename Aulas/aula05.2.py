#Função range () - gerador de listas
#range(inicio, limite (estritamente menor), salto) OU
#range(limite) - de zero ao limite

#Gerador de Tabuada com FOR
n = int(input())
print(f"\nTabuada do {n}:\n")

for i in range(0, 11, 1):
    mult = n*i 
    print(f"{n} x {i} = {mult}")
    
print("\nFIM")


#Gerador de Tabuada com WHILE
o = 0
n = int(input())
print(f"\nTabuada do {n}:\n")

while (o <= 10):
    mult = n*o
    print(f"{n} x {o} = {mult}")
    o += 1

print("\nFIM")
