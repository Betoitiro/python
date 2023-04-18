#primeiro adiciona os intens ao dicionario.
n = {
    'jaguar typer 7' : 180000,
    'corolla': 13000,
    'jetta' : 230000,
    'golt gli' : 150000
}

#for para mostrar os carros e os numeros, usando as chaves
for nome in n.keys():
    print('{}, custa = R${:.2f}'.format(nome, n[nome]))