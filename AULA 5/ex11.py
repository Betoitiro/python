def palavra_frequente(list):
    contar = {}
    for palavra in list:
        if palavra in contar:
            contar[palavra] +=1
        else:
            contar[palavra] =1

    return max(contar, key=contar.get)

list = ['branco', 'vermelho', 'vermelho', 'azul', 'verde', 'amarelo', ' vermelho']
palavra = palavra_frequente(list)
print(palavra)