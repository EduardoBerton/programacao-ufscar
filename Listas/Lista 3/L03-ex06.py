#Exercício 1131 - Grenais
GOLS_I = 0
GOLS_G = 0
SIM_NAO = 1
GRENAIS_I = 0
GRENAIS_G = 0
EMPATES = 0

while(SIM_NAO == 1): 
    GOLS_I,GOLS_G = map(int,input().split())

    if (GOLS_I > GOLS_G):
        GRENAIS_I += 1
    elif (GOLS_I < GOLS_G):
        GRENAIS_G += 1
    else: 
        EMPATES += 1
        

    print("Novo grenal (1-sim 2-nao)")
    SIM_NAO = int(input())



print(f"{GRENAIS_I + GRENAIS_G + EMPATES} grenais")
print(f"Inter:{GRENAIS_I}")
print(f"Gremio:{GRENAIS_G}")
print(f"Empates:{EMPATES}")

if (GRENAIS_I > GRENAIS_G):
    print("Inter venceu mais")
elif (GRENAIS_I < GRENAIS_G):
    print("Gremio venceu mais")  
else: 
    print("Não houve vencedor")  

