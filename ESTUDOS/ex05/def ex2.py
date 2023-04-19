#lista de compras
#vai querer saber o maior valor do produto
#se possivel mostrar o nome, quantidade e valor

def compras_valor(list):
    maior = list[0]
    for valor in list:
        if valor >maior:
            maior = valor
    return maior

num = [2,3,6,8,10,93,34,36]
maior = compras_valor(num)
print(maior)