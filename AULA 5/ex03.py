listas = [1, 2, 3, 4, 5, 6]
soma_pares = 0

for numero in lista:
    if numero % 2 == 0:
        soma_pares += numero

print(soma_pares)