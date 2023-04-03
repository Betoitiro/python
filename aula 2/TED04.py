#Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere
#o valor zero como positivo).

n = float(input("digite um numero: "))
if n > 0:
    print("o numero {}  é positivo!".format(n))
else:
    print("o numero {} é negativo!".format(n))



'''Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
calcule e escreva o custo total da compra.'''

nm = int(input("digite quantas maçãs foram compradas: "))
m = 1.30
m2 = 1.00
s = nm * m
if nm >= 12:
    s2 = nm* m2
    print("o cliente comprou {} maçãs e o valor da sua compra foi de R${:.2f}". format(nm,s2))
else:
    print("o cliente comprou {} maçãs e o valor da sua compra foi de R${:.2f}". format(nm,s))

