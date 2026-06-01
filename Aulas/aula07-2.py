#Concatenação: A + B = [a1, a2, a3, b1, b2, b3]
#Repetição: A*2 = [a1, a2, a3, a1, a2, a3]

#a.append(x) ---- Adciona o elemento x no final da lista a
# a.insert(x,y) ---- Coloca o elemento y na posição x
# print(a.pop(x)) --- Tira o elemento da posição x na lista a e mostra
# a.extend(b) ---- Extende a lista a com os elementos de b (a += b)
# del(a[x]) ---- deleta x de a 


#Apelidos de lista 
#a = [1, 2, 3]
#b = a --- qualquer alteração feita em um afeta o outro

#Fatiamento de listas ---- lista[i:f]
#Clonagem com fatiamento ---- b = a[:] (b é uma fatia do começo ao final de a)

a = [1, 2, 3, 4, 5]
b = a[2:5]

b[2] = 2

print(a)

#Atualização de lista
#Salto :: 

print(a[-2:-1])
a1 = a[::2]
a2 = a[::-1]

print(a2)


