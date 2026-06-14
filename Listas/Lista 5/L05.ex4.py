#Exercicio 1179 - Prenchimento de Vetores IV
#To read 15 numbers, separate into two arrays "par" and "impar", but the maximum lenght of them is 5 numbers  and the arrays must be cleaned to make room for the next numbers

i = 0
par = []
impar = []

while i < 15: 
    N = int(input())

    # N é par? 
    if N/2 == 0: 
        # vetor par tem menos que cinco números?
        if len(par) < 5: # Sim - põe no par 
            par.append(N)
        else: # Não - limpa o par (pop ou criar vetores pra armazenar)
            par.pop()
            
            par.append(N)

        

    # ou não (é impar)? Põe no ímpar
    else: 
        impar.append(N)

    






