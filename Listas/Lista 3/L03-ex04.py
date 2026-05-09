#Exercício 1079 - Médias Ponderadas

N = int(input())

I = 0
while (I < N):  
    A,B,C = map(float, input().split())

    MED = (2*A + 3*B + 5*C)/10

    print("%.1f" %MED)

    I += 1