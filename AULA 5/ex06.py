est = [{'nome': 'maça', 'preço':2.0, 'quantidade':5},
       {'nome': 'banana', 'preço': 1.5, 'quantidade': 10}]

total = 0.0
for produto in est:
    v_p = produto['preço'] * produto['quantidade']
    total += v_p

print('o valor total do produto é R${:.2f}'.format(total))
