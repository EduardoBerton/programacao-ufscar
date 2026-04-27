#Exercício 1117 - Validação de Notas

nota1 = float(input("Nota 1: "))
while(nota1 < 0 or nota1 > 10):
    print("Nota inválida.")
    nota1 = float(input("Nota 1: "))

nota2 = float(input("Nota 2: "))
while(nota2 < 0 or nota2 > 10):
    print("Nota inválida.") 
    nota2 = float(input("Nota 2: "))  

media = (nota1 + nota2) / 2 
print(f"Média: {media}")     


