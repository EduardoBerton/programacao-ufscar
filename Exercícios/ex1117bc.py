#Exercício 1117 - Validação de Notas

nota1 = float(input("Nota 1: ").replace(",","."))
while(nota1 < 0 or nota1 > 10):
    print("Nota inválida.")
    nota1 = float(input("Nota 1: ").replace(",","."))

nota2 = float(input("Nota 2: ").replace(",","."))
while(nota2 < 0 or nota2 > 10):
    print("Nota inválida.") 
    nota2 = float(input("Nota 2: ").replace(",","."))  

media = (nota1 + nota2) / 2 
print(f"Média: {media}")     


