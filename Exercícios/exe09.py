print("Verificar existência e tipo de Triângulo")

l1 = float(input("Informe o Lado 1: "))
l2 = float(input("Informe o Lado 2: "))
l3 = float(input("Informe o Lado 3: "))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2): 

    if (l1 != l2 != l3) and (l1 != l3):
        print ("Triângulo escaleno de lado: %.1f, %.1f e %.1f" % (l1, l2, l3)) 

    elif (l1 != l2 == l3) or (l2 != l3 == l1) or (l3 != l1 == l2):
        print ("Triângulo isóceles de lados: %.1f, %.1f e %.1f" % (l1, l2, l3))

    elif (l1 == l2 == l3): 
        print ("Triângulo equilátero de lado: %.1f, %.1f e %.1f" % (l1, l2, l3))   

else: 
    print("Não é um triângulo")

    
