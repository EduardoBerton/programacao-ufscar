print("Calculo da conta telefonica por minutos usados")

tempo = int(input("Por quantos minutos você utilizou o telefone: "))

if (tempo < 200): 
    conta = float(tempo * 0.2)
    print("Valor da conta: R${:.2f}" .format(conta))
elif ( 200 <= tempo <= 400): 
    conta = float(tempo * 0.18)
    print("Valor da conta: R${:.2f}" .format(conta))
elif (tempo > 400): 
    conta = float(tempo * 0.15)
    print("Valor da conta: R${:.2f}" .format(conta)) 