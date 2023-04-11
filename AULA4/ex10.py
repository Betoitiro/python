
print("Digite os nomes: ")
nomes = []
while True:
    nome = input()
    if nome == "":
        break
    nomes.append(nome)


nomes_unicos = []
for nome in nomes:
    if nome not in nomes_unicos:
        nomes_unicos.append(nome)


print("Nomes únicos:")
for nome in nomes_unicos:
    print(nome)
