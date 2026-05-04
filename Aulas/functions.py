#input().replace('x','y') -> Substitui x por y na variável

#input().split(X) -> Separa um string em vários a cada X

#map(int, input()) -> Converte tudo do input pra int 

X, Y, Z = map(float, input("Digite três números: ").replace(",", ".").split())

print(X, type(X))
print(Y, type(Y))
print(Z, type(Z))

#\n (Escape) -> Quebra de linha

#sorted(var, Reverse=True) -> Organiza a lista em ordem decrescente

#X = lista[0] -> Atribui a X o 1° valor da lista