#Exercício 1134 - Tipo de Combustível

I = 0
ALC = 0
GAS = 0
DIE = 0

while (I != 4): 
    I = int(input())

    while (I < 1 or I > 4):
        I = int(input())
    if (I == 1):
        ALC += 1
    elif (I == 2): 
        GAS += 1
    elif (I == 3): 
        DIE += 1
    elif(I == 4):
        break
            

print("MUITO OBRIGADO")
print(f"Alcool: {ALC}")
print(f"Gasolina: {GAS}")
print(f"Diesel: {DIE}")

