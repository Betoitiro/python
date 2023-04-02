
print('reajuste salarial de 30%')
print(40*'<-->')

nome = str(input(' boa noite,, voce poderia digitar seu nome >   '))
print(40*'<-->')
print('seja bem vindo {}!' .format(nome))
salario = float(input('informe o calor bruto do seu salario:'))
aumento = salario + (salario*30/100)

print(3*'-              -               -               -')

print('o seu salario era de {:.2f}, com u aumento de 30% ficou {:.2f}'.format(salario,aumento))