estoque = [{'nome': 'maçã', 'preço': 2.0, 'quantidade': 5}, {'nome': 'banana', 'preço': 1.5, 'quantidade': 8}, {
    'nome': 'laranja', 'preço': 1.9, 'quantidade': 13}, {'nome': 'pessego', 'preço': 4.5, 'quantidade': 3}]

total = 0.0
for pr in estoque:
    v_p = pr['preço'] * pr['quantidade']
    total += v_p


print('o valor do estoque é de R${:.2f}'.format(total))