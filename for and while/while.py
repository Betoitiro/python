#script que calcule o fatorial do numero

numero = int(input("Digite um numero: "))
fatorial = 1 #estabelecer uma variavel ao fatorial
c = 1 #variavel para percorrer a lista

while c <= numero:
    fatorial *=c
    c +=1 #calcular o produto

print(f"O fatorial {numero} é {fatorial}")