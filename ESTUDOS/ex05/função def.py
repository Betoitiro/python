#imprimir um maior valor da lista

def maior_valor(list):
    maior = list[0]
    for valor in list:
        if valor > maior:
            maior = valor
    return maior


num = [20,36,25,27,59,1023,10205,2003,25893,125893]
maior = maior_valor(num)
print("o vamor valor é: ", maior)