#Exercício 1278 - Justificador II

N = 1
while (N != 0) == True: 
    N = int(input())

    texto = []
    maior_linha = 0
    
    for i in range(N):
        linha = " ".join(input().split())
        texto.append(linha)

        if len(linha) > maior_linha:
            maior_linha = len(linha)
    
    for linha in texto: 
        justificar = (maior_linha - len(linha))*(" ")
        print(justificar + linha)
    print()

    






