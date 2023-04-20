def compras(list):
    maior = list[0]
    for numero in list:
        if numero > maior:
             maior = numero
    return maior

list = [5,23,69,33,66,393,3256,325,363639]
maior = compras(list)
print("o maior numero da lista é: ", maior)
