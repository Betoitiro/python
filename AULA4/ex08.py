#como fazer um programa que leia uma string e verifique se ela é um palíndromo.


palavra = input("Digite uma palavra: ")


palavra = palavra.replace(" ", "").lower()


if palavra == palavra[::-1]:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
