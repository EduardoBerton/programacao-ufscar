#Exercício 1078 - Tabuada

N = int(input())
while (N < 2 or N > 1000):
  N = int(input())

for i in range(1,11,1):
  RES = N*i
  print(f"{i} x {N} = {RES}")