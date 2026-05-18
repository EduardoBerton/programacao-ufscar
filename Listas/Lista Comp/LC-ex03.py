#Exercicio 1021 - Baknotes and coins
N = float(input())

while (N < 0 or N > 1000000.00):
    N = float(input())

print("NOTAS:")

notas = [100, 50, 20, 10, 5, 2]

for nota in notas: 
    qtd = int(N // nota)
    print("%.d nota(s) de R$ %.2f" %(qtd, nota))
    N %= nota

print("MOEDAS:")

moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

for moeda in moedas: 
    qtd = int(N // moeda)
    print("%.d moeda(s) de R$ %.2f" %(qtd, moeda))
    N %= moeda