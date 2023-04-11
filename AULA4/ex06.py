#Intermediário: Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1500,00, o aumento é de 10%. Para salários inferiores ou iguais a R$1500,00, o aumento é de 15%.
salario= float(input("digite o seu salario: "))
if salario >= 1500:
    aumento = salario * (1.10)
    print("o salario passara a ser {:.2f}".format(aumento))
elif salario < 1500:
    nvs = salario * (1.15)
    print("o salario passara a ser {:.2f}".format(nvs))