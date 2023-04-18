dados = {'EUA': ['nova iorque', 'los angeles', 'chicago'], 'BRASIL': ['são paulo', 'belo horizonte', 'rj']}
pol = {'nova iorque': 82000, 'los angeles': 500000, 'chicago': 54060000, 'são paulo': 1400000, 'belo horizonte': 203000, 'rj': 2000000}

maior_cidade = {}
for pais, cidade in dados.items():
    cidade_maior = ''
    populacao_maior = 0

    for cid in cidade:
        if pol[cidade] > populacao_maior:
            cidade_maior = cidade
            populacao_maior = pol[cidade]
    maior_cidade[pais] = cidade_maior

    print(maior_cidade)
