print("Aumento pelo tempo de trabalho")

sal = float(input("Informe seu Salário: "))
dias = int(input("Tempo de trabalho em dias: "))

anos = dias/365
meses = (dias%365)/30
dias = (dias%365)%30

if (anos >= 5):
    nsal = sal * 1.2
    print("Você trabalhou por %d anos, %d meses e %d dias. Seu novo salário é: %.2f" % (anos, meses, dias, nsal))
elif ( 1 <= anos < 5):
    nsal = sal * 1.1
    print("Você trabalhou por %d anos, %d meses e %d dias. Seu novo salário é: %.2f" % (anos, meses, dias, nsal))
else: 
    print("Você trabalhou por %d anos, %d meses e %d dias. Toma vergonha na cara rapaz" % (anos, meses, dias))
