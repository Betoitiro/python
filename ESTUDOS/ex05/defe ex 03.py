#encontrar o produto na lista que possui a o maior valor
#esse sera encontrado, mutiplicando o total(unds) por preço
#mostrar o valor total da compra o final



def maior_preço(list):
    maior = None
    for item in list:
        total = item['preço'] * item['quantidade']
        item['total'] = total
        if maior is None or total > maior['preço'] * maior['quantidade']:
            maior = item
    return maior
produto = [
    {'produto': 'maça', 'preço': 2.5, 'quantidade': 10},
    {'produto': 'pêra', 'preço': 3.0, 'quantidade': 15},
    {'prduto': 'maracuja', 'preço': 4.0, 'quantidade':12}
]

maior = maior_preço(produto)

print('O produto que deu o maior valor foi {},\n'
      'e o total dessa compra'
      ' foi de R${:.2f}'.format(maior,maior['total']))