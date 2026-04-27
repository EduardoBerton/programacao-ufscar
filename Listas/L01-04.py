#Exercício 1019 - Conversão de Tempo

N = int(input("Tempo[s]: "))

hours = N/3600
minutes = (N%3600)/60
seconds = (N%3600)%60

