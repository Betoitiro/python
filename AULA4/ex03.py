#Fácil: Crie um programa que solicite o nome e a idade do usuário e informe se ele pode dirigir um veículo.

nome = str(input("Informe seu nome: "))
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("{}, voce pode dirigir um veiculo". format(nome))
else:
    print("{}, voce não pode dirigir um veiculo".format(nome))