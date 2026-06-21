#Exercício 2815 - Digitador Gago

texto_gago = input().split(" ")
texto_normal = []

for palavra in texto_gago: 
    if palavra[0:2] == palavra[2:4]:
        palavra = palavra[2:]
        texto_normal.append(palavra)
    else: 
        texto_normal.append(palavra)

traducao = " ".join(texto_normal)
print(traducao)
    


    


