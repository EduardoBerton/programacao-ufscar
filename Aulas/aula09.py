#DICIONÁRIOS
#nome_dicionario = {chave: valor, chave: valor, ...}
#chave --> string(imutavel)
#valor --> qualquer tipo

arroz = {} #dicionario vazio

arroz = {"nome": "algum", "age": 90, "hobbies": ["alguns", "outros", "mais"]}

for chave in arroz: 
    print(arroz[chave])