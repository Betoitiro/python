#calcular todos os numeros multiplos de algum numero, no intervalo desejado

#todos os multiplos de 3 entre 1 a 500
cont =0
soma = 0
for i in range(1 ,501, 2):
    if i %3 ==0:
        cont = cont+1
        soma = soma + i
print("A soma dos {} valores é de {}".format(cont,soma))
