def palavra_frequente(list):
    contar = {} #serve para usar de chave para string no sistema
    for palavra in list:
        if palavra in contar:
            contar[palavra] +=1
        else:
            contar[palavra] =1

    return max(contar, key=contar.get) #atrubui a variavel contar a chave

list = ['branco', 'vermelho', 'vermelho', 'azul', 'verde', 'amarelo', ' vermelho']
palavra = palavra_frequente(list)
print(palavra)