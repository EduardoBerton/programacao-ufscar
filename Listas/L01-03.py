#Exercício 1017 - Gasto de Combustível

spent_time = int(input("Tempo gasto(horas): "))
avg_speed = int(input("Velocidade média(km/h): "))

tot_distance = spent_time * avg_speed
fuel_spent = tot_distance / 12

print("Gasto de combustível(L/km): %.3f" %(fuel_spent))







