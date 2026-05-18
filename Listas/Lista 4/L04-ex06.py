#Exercício 1094 - Experiencias

N = int(input())

while (N < 1 or N > 15):
    print("ENTRADA INVALIDA")
    N = int(input())

coelhos = 0
ratos = 0
sapos = 0


for i in range (1, (N + 1), 1):
    amount, type_ = input().split()
    amount = int(amount)
    if (type_ == "C"):
        coelhos += amount
    elif (type_ == "R"):
        ratos += amount
    elif (type_ == "S"):
        sapos += amount


total = coelhos + ratos + sapos
p_coelhos = coelhos/total*100
p_ratos = ratos/total*100
p_sapos = sapos/total*100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print("Percentual de coelhos: %.2f %%" % (p_coelhos))
print("Percentual de ratos: %.2f %%" % (p_ratos))
print("Percentual de sapos: %.2f %%" % (p_sapos))