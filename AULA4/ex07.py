#Intermediário: Faça um programa que leia uma lista de números inteiros e informe qual o maior valor e qual o menor valor da lista
lists = [8,6,9,10,11,25,99]

maior = lists[0]
menor = lists[0]
for numero in lists:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("o menor numero é", menor)
print("o maior numero é ", maior)