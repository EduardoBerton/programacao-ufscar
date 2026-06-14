#Teste contador de caracteres que imprime as maiores frequencias

text = input("Texto: ").replace(" ","")
letras = {} #a: x, b: y...


for letra in text:

    if letra not in letras:         #Se não está no dicionário -> crio uma chave com valor 1
        letras[f"{letra}"] = 1  
    else:                           #Se está -> atualizo o valor da chave em 1
        letras[f"{letra}"] += 1

maior_freq = 0

for letra in letras:                #Pra cada chave do dicionário, verifico a maior frequencia
    if letras[letra] > maior_freq:
        maior_freq = letras[letra]

frequentes = ""

for letra in sorted(letras):        #Pra cada letra na lista ordenada, verifico frequencias iguais e imprimo
    if letras[letra] == maior_freq:
        frequentes += letra

print("Letras mais frequentes: ", frequentes)
print("Frequencia: ", maior_freq)







