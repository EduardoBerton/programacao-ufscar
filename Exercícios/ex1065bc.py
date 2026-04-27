#Exercício 1065 - Even Numbers
i = 1 
even = 0

while(i <= 5):

    num = int(input())
    if (num%2 == 0): 
         even += 1

    i += 1



print(f"{even} valores pares")   