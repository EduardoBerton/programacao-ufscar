#Exercício 1273 - Justificador

N = 1
while (N != 0) == True: 

    N = int(input())
    palavras = []

    for i in range(N):
        palavras.append(input().upper())

    maior_palavra = ""
    tamanho_maior = 0

    for palavra in palavras:
        if len(palavra) > tamanho_maior:
            maior_palavra = palavra
            tamanho_maior = len(maior_palavra)

    for palavra in palavras: 
        if len(palavra) < tamanho_maior:
            justificar = (tamanho_maior - len(palavra))*(" ")
            print(justificar + palavra)
        else: 
            print(palavra)
    print()


