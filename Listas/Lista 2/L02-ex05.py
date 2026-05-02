#Exercício 1046 - Tempo de Jogo

start, end = map(int, input().split())

if (start > end): 
    time = (24 - start) + end
    print("O JOGO DUROU %d HORA(S)" %time)
elif (start < end): 
    time = end - start
    print("O JOGO DUROU %d HORA(S)" %time)
elif (start == end): 
    time = 24
    print("O JOGO DUROU %d HORA(S)" %time)
    
