p1 = float(input("Nota da P1: "))
p2 = float(input("Nota da p2: "))

med = (p1 + p2)/2

if (med >= 6): 
    print("Média: %.2f. Aprovado!" % med)
elif (5 <= med < 6): 
    print("Média: %.2f. Pode fazer a Recuperação" % med)
elif (med < 5): 
    print("Média: %.2f. Desista dos seus sonhos e morra" % med)
