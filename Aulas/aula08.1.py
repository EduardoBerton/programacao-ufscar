#MATRIZES - matriz = [[1,0,0], [0,1,0], [0,0,1]]
#linha_0 = matriz[0]
#matriz[2][1] - elemento na linha 2(3°) e coluna 1(2°)

#LER e IMPRIMIR uma matriz 3X2

mat = []
n = int(input("Linhas: "))
m = int(input("Colunas: "))

for i in range(n):
    linha = []
    for j in range(m):
        num = int(input())
        linha.append(num)
    mat.append(linha)

print("MATRIZ: ")

for i in range(n):
    for j in range(m):
        print(mat[i][j], end = " ")
    print()
        
