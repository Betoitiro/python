#Fácil: Faça um programa que calcule a média aritmética de 4 notas e informe se o aluno foi aprovado (média maior ou igual a 7) ou reprovado.

n1 = float(input("digite sua primeira nota: "))
n2 = float(input("digite sua segunda nota: "))
n3= float(input("digite a sua terceira nota: "))
n4 = float(input("digite sua quarta nota"))
media = (n1 + n2 + n3 + n4)/4
if media >= 7:
    print("aprovado, media {}".format(media))
else:
    print("reprovado, media {}".format(media))