#Exercício 1043 - Triângulo

# Triângulo ABC existe se: a+b>c e a+c>b e b+c>a 

A,B,C = map(float, input().replace(',','.').split())

if (A + B > C and A + C > B and B + C > A):
    per_tri = A + B + C
    print("Perimetro = %.1f" %(per_tri))
else: 
    area_trp = ((A+B)*C)/2
    print("Area = %.1f" %area_trp)
    
