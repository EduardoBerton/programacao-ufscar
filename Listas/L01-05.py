#Exercício 1020 - Idade em dias

idade_em_dias = int(input())

anos = idade_em_dias/365
meses = (idade_em_dias%365)/30
dias = (idade_em_dias%365)%30

print("%d ano(s)" %(anos))
print("%d mes(es)" %(meses))
print("%d dia(s)" %(dias))
