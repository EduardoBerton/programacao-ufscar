#TUPLAS - Imutável, dados heterogêneos
###tupla = (a, b, c, d) 
#OPERAÇÕES - indexação, fatiamento, len, concatenação...
#Elementos acessados por índices - tupla[0]

#Empacotamento


#Tuplas e Listas
L = [1, 2, 3]

T = (L, 3, 2)
print(T)

T[0][1], T[0][2] = T[0][2], T[0][1]

a, b, c = T[0], T[1], T[2]

print(T)
