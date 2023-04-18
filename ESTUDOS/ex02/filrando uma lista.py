#vamos primeiro somar os numeros pares da lista
# e no mesmo programa usar o sistemas para pegar o taltal de impares

lists = [ 1, 2, 6, 8, 17, 14, 25, 26, 23, 36]
sp = 0 # variavel responsavel pelo total de pares.
si = 0 # variavel responsalvel pelo tatal de impares
s = 0 #programa para somar ambos (impares e pares)

for num in lists:
    if num % 2 == 0: #condição para que caso o numero seja par
        sp += num   #condição para que some a variavel dos pares, se o numero for par
    elif num %2 != 0:
        si += num

s = sp + si
m =int(s/2)

print("o total de numeros pares é de: ", sp)
print("o total de numeros impares é de: ", si)
print("o total de impares e pares é de: ", s)
print("a medi de ambos é de: ", m)