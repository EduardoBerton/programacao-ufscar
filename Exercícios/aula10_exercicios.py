#Ler duas strings e gerar outra com caracteres comuns

# string_1 = input()
# string_2 = input()

# string_3 = ""

# for caractere in string_1: 
#     if caractere in string_2: 
#         string_3 += caractere


# print(string_3)

#EXERCICI0 2 - Ler 2 strings e gerar uma terceira com os caracteres que aparecem em apenas uma delas

# string_1 = input()
# string_2 = input()

# string_3 = ""

# for caractere in string_2: #Lembra do AND
#     if caractere not in  string_1:
#         string_3 += caractere

# for caractere in string_1: 
#     if caractere not in string_2: 
#         string_3 += caractere


# print(string_3)

#EXERCICIO 3 - Ler 2 strings e gerar outra na qual os caracteres da segunda foram retirados da primeira

string_1 = input()
string_2 = input()

string_3 = ""

for caractere in string_1: 
    if caractere not in string_2:  
        string_3 += caractere

print(string_3)