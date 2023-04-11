#Fácil: Escreva um programa que receba a idade de uma pessoa e informe se ela é maior de idade ou não.

idade = int(input("digite sua idade: "))
if idade < 18:
    print("não é maior de idade")
else:
    print("maior de idade")