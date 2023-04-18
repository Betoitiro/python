#nessa questão precisei do auxilio do chat gpt

def ordenar_por_tamanho(lista):
    return sorted(lista, key=len, reverse=True)


lista = ['casa', 'carro', 'abacate', 'pipoca']
print(ordenar_por_tamanho(lista))
