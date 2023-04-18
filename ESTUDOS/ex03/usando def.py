#pegando a diferença de preço
tuple = ((8,10), (15,20))

def ts(tuple):
    total = 0
    for inicio, fim in tuple: #nesse trecho, a palavra fim e inicio, pode ser documentada da maneira que for mais compativel
        total += fim - inicio #contanto que elas sigam esse sentido
    return total
print(ts(tuple))

