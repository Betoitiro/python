#esse programa vai perguntar o nome/palavra ao usuario, e vai mostrar quantas consoantes e quantas vogais possui

p = str(input("Digite uma palavra: ")).lower()

#vamos estabelecer a quantidade de vogais e de consoantes que possuimos antes de apresentar o for
vogais = 0
consoante = 0 

#estabelece uma variavel que sera letra, que esta diretamente ligada a p
#depois se cria uma condição para que se caso tenha as letras, acresente na variavel.
for letra in p:
    if letra in "aeiou":
        vogais+=1
    else:
        consoante+=1

print(vogais)
print(consoante)