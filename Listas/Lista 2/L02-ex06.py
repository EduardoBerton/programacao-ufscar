#Exercício 1048 - Aumento de Salário

SAL = float(input())

if(0 <= SAL <= 400.00): 
    RATE = 15
    NSAL = (1 + RATE/100)*SAL
    
    print("Novo salario: %.2f" %NSAL)
    print("Reajuste ganho: %.2f" %(NSAL-SAL))
    print(f"Em percentual: {RATE} %")

elif(400.01 <= SAL <= 800.00): 
    RATE = 12
    NSAL = (1 + RATE/100)*SAL
    
    print("Novo salario: %.2f" %NSAL)
    print("Reajuste ganho: %.2f" %(NSAL-SAL))
    print(f"Em percentual: {RATE} %")

elif(800.01 <= SAL <= 1200.00): 
    RATE = 10
    NSAL = (1 + RATE/100)*SAL
    
    print("Novo salario: %.2f" %NSAL)
    print("Reajuste ganho: %.2f" %(NSAL-SAL))
    print(f"Em percentual: {RATE} %")

elif(1200.01 <= SAL <= 2000.00): 
    RATE = 7
    NSAL = (1 + RATE/100)*SAL
    
    print("Novo salario: %.2f" %NSAL)
    print("Reajuste ganho: %.2f" %(NSAL-SAL))
    print(f"Em percentual: {RATE} %")

if(SAL > 2000.00): 
    RATE = 4
    NSAL = (1 + RATE/100)*SAL
    
    print("Novo salario: %.2f" %NSAL)
    print("Reajuste ganho: %.2f" %(NSAL-SAL))
    print(f"Em percentual: {RATE} %")
