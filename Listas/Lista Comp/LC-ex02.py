#Exercício 1036 - Bhaskara's Formula
A,B,C = map(float, input().split())

if (A != 0 and B**2 > 4*A*C):
    R1 = (-B + ((B**2 - 4*A*C)**(1/2)))/(2*A)
    R2 = (-B - ((B**2 - 4*A*C)**(1/2)))/(2*A)

    print("R1 = %.5f" %(R1))
    print("R2 = %.5f" %(R2))
else: 
    print("Impossivel calcular")