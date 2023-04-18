dados = {'Brasil': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'], 'EUA': ['Nova Iorque', 'Los Angeles', 'Chicago']}

populacao = {'São Paulo': 22000000, 'Rio de Janeiro': 13000000, 'Belo Horizonte': 2500000, 'Nova Iorque': 8400000, 'Los Angeles': 4000000, 'Chicago': 2700000}

mais_populosas = {}
for pais, cidades in dados.items():
    cidade_mais_populosa = ''
    populacao_cidade_mais_populosa = 0
    for cidade in cidades:
        if populacao[cidade] > populacao_cidade_mais_populosa:
            cidade_mais_populosa = cidade
            populacao_cidade_mais_populosa = populacao[cidade]
    mais_populosas[pais] = cidade_mais_populosa

print(mais_populosas)
