#Dicionários

palavra = input()
dict = {}

for caractere in palavra: 
    if caractere in dict: 
        dict[caractere] += 1
    else:
        dict[caractere] = 1
    print(dict)