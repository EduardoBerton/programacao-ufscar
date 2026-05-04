#Função range () - gerador de listas
#range(inicio, limite (estritamente menor), salto) OU
#range(limite) - de zero ao limite

n = int(input())

for i in range(0, 11, 1):
    mult = n*i 
    print(f"{n} x {i} = {mult}")

