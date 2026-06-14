#DICIONÁRIOS
#nome_dicionario = {chave: valor, chave: valor, ...}
#chave --> string(imutavel)
#valor --> qualquer tipo

arroz = {} #dicionario vazio

arroz = {"nome": "algum", "age": 90, "hobbies": ["alguns", "outros", "mais"]}

#Printar valores das chaves
for chave in arroz: 
    print(arroz[chave])

#Printar nome das chaves
for chave in arroz: 
    print(chave)