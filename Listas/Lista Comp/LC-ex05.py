#Dicionários
#acessar estoque analisa as chaves
#acessar estoque[prod] analisa o valor da chave específica

estoque = {"maca": 89, "banana": 66, "laranja": 45, "pera": 27}

print("VENDA")
print("Digite PRODUTO e QTD: ")

venda = input().split()
prod = venda[0]
qtd = int(venda[1])

while prod not in estoque: 
    prod = input(f"Têm {prod} não: ")
    if prod in estoque: 
        qtd = int(input("Quantas cê queria mêmo: "))

while qtd > estoque[prod]: 
    qtd = int(input(f"Têm {qtd} não: "))

print(f"Compra: {qtd} {prod}(s)")





    

            
        
        