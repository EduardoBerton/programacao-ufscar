#Justificar texto (colocar espaço antes ou depois)
# text.ljust(X) - justifica X casas à esquerda
# text.rjust(X) - Justifica X casas à direita
# text.center(X) - justifica no centro de X casas
# F-Strings - f"{text:>X}" (>, <, ^ )

texto = input("Texto: ")
justificar = int(input())
empty_spaces = (justificar - len(texto))*(" ")

texto = empty_spaces + texto
print(texto)


#JUNTAR TEXTO 
# .join(...)