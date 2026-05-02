#Exercício 1045 - Tipos de Triângulos

A,B,C = map(float, input().split())

#Se A < B coloque B na frente
if (A < B):
    A,B = B,A
if (A < C):
    A,C = C,A
if (B < C): 
    B,C = C,B

if (A >= B + C): 
    print("NAO FORMA TRIANGULO")
elif (A**2 == B**2 + C**2):
    print("TRIANGULO RETANGULO")
elif (A**2 > B**2 + C**2): 
    print("TRIANGULO OBTUSANGULO")
elif (A**2 < B**2 + C**2): 
    print("TRIANGULO ACUTANGULO")


if (A == B == C):
    print("TRIANGULO EQUILATERO")
if (A == B != C or A == C != B or B == C != A):
    print("TRIANGULO ISOSCELES")
