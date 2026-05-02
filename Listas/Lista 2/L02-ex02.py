#Exercício 1042 - Sort Simples

X, Y, Z = map(int, input().split())

if (X > Y > Z): 
    print(f"{Z}\n{Y}\n{X}")
    print()
    print(f"{X}\n{Y}\n{Z}")
elif (X > Z > Y): 
    print(f"{Y}\n{Z}\n{X}")
    print()
    print(f"{X}\n{Y}\n{Z}")

elif (Y > X > Z): 
    print(f"{Z}\n{X}\n{Y}")
    print()
    print(f"{X}\n{Y}\n{Z}")
elif (Y > Z > X): 
    print(f"{X}\n{Z}\n{Y}") 
    print()
    print(f"{X}\n{Y}\n{Z}")

elif (Z > X > Y): 
    print(f"{Y}\n{X}\n{Z}")
    print()
    print(f"{X}\n{Y}\n{Z}")
elif (Z > Y > X): 
    print(f"{X}\n{Y}\n{Z}")
    print()
    print(f"{X}\n{Y}\n{Z}")        