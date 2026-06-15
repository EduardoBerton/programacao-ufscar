#Exercício 1255 - Frequencia de letras

N = int(input())

for i in range(N):

    text = input().replace(" ","").lower()
    letras = {}

    for letra in text:
        if letra not in letras: 
            letras[f"{letra}"] = 1
        else: 
            letras[f"{letra}"] += 1
    
    maior_freq = 0

    for letra in letras:
        if letras[letra] > maior_freq:
            maior_freq = letras[letra]
    
    mais_freq = ""

    for letra in sorted(letras):
        if letras[letra] == maior_freq:
            mais_freq += letra

    print(mais_freq)