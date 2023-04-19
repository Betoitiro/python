def maior_preço(list):
    maior = None
    for item in list:
        total = item['preço'] * item['quantidade']
        item['total'] = total # adiciona a chave 'total' com o valor da multiplicação
        if maior is None or total > maior['preço'] * maior['quantidade']:
            maior = item
    return maior

produto = [
    {'produto': 'maça', 'preço': 2.5, 'quantidade': 10},
    {'produto': 'pêra', 'preço': 3.0, 'quantidade': 15},
    {'produto': 'maracuja', 'preço': 4.0, 'quantidade': 12}
]

maior = maior_preço(produto)

print("Produto com maior valor total:", maior)
print("Valor total:", maior['total']) # mostra o valor total do produto com maior valor
