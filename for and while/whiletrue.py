#usando while como condição verdadeira
#vai ler uma lista  somar com o numero digitado pelo usuario

#ese prorama vai pegar os numeros do usuario digitar no loop while e somalos com a variavel s/

num =[] #comando que vai listar os valores digitados em n
s = 2 #soma feita no final

while True:
    n = input("Digite um numero(ou 'fim' para encerrar): ")
    if n == 'fim': #condição para que quando chegue ao fim os numeros parem se ser acrecentados na lista
        break
    num.append(int(n))  #comando que acrecenta n dentro da lista de num

for n in num: #loop para que n recebesse os elementos da lista a cada interação do loop
    s +=n #soma dos elementos

print(f"A soma dos numeros é {s}")