#Exercicio 2242 - Huaauhahhuahau
#ignorando as consoantes, verificar se a ordem natural é igual a ordem reversa

laugh = input()
vowels = ["a","e","i","o","u"]
laugh_vowels = []

for letter in laugh: 
    if letter in vowels:
        laugh_vowels.append(letter)

natural_order = laugh_vowels
reverse_order = laugh_vowels[::-1]

if  natural_order == reverse_order: 
    print("S")
else: 
    print("N") 