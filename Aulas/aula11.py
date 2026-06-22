#FUNÇÕES 
#Definição da função: 
# def nome_da_funcao (parametro): 
    #instrução 1
    #instrução 2
    #return
# Chamada da função:
# nome_da_funcao(parametro)

nome_1 = input().lower()
nome_2 = input().lower()


def cu_ou_nao_cu():
    if nome_1 or nome_2 == "thiago" and nome_2 or nome_1 == "henri":
        print("namoram")
    else: 
        print("Já se beijaram")

cu_ou_nao_cu()