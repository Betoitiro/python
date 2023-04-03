print(40*'--')

print('Olá, seja vemm vindo ao aluguel de veiculos.com!')
print("por gentileza, poderia informar seu nome?")
nome= str(input("nome: "))


print(40*'---')

print("seja bem vindo {}, esses são os modelos disponiveis: ".format(nome))

a = ("MODELO A =  onix 2016 por R$120,00 a diaria")

b = ("MODELO B =  onix 2022 por R$150,00 a diaria")

c= ("MODELO C =  gol 2015 por R$100,00 a diaria")

d = ("MODELO D = gol 2022 por R$140,00 a diaria")

print(a)
print(b)
print(c)
print(d)

print(40*'---')




m = str(input("Digite o modelo que voce procura alugar:  ")).lower() #comando ultilizado para evitar erros de escrita 
#os modelos de carros foram selecionados apartir do if/elif, quando o cliente escolher na tabela acima e der o comando na pergunta
#o modelo sera selecionado automaticamente
if m =="modelo a":
    print("o modelo escolhido foi o {}".format(a))
elif m == "modelo b":
    print("o modelo escolhido foi o {}".format(b))

elif m == "modelo c":
    print("o modelo escolhido foi o {}".format(c))

elif m =="modelo d":
    print("o modelo escolhido foi o {}".format(d))

print(40*'---')

dia = int(input("digite a quantidade de diarias que voce deseja passar: "))
#o dia, corresponde as diarias que o cliente passara com o carro alugado
if m == "modelo a":
    d= dia*120
    print("o modelo escolhido foi {} e sua diaria saira na faixa de R${:.2f}, sujeita alterção devido a quantidade de km rodados!".format(m,d))

elif m =="modelo b":
    d1= dia*150
    print("o modelo escolhido foi {} e sua diaria saira na faixa de R${:.2f}, sujeita alterção devido a quantidade de km rodados!". format(m,d1))

elif m =="modelo c":
    d2 = dia*100
    print("o modelo escolhido foi {} e sua diaria saira na faixa de R${:.2f}, sujeita alterção devido a quantidade de km rodados!". format(m,d2))

elif m == "modelo d":
    d3 = dia*140
    print ("o modelo escolhido foi {} e sua diaria saira na faixa de R${:.2f}, sujeita alterção devido a quantidade de km rodados!". format(m,d3))

#cada carro possui um valor diferente para o alufguel

print("certo, agora podemos seguir para o envio de dados para finalizarmos o aluguel!!")

#controle de dados pro cliente
#banco de dados do sistema
print("boa tarde!")
print("por gentileza, poderia nos informar seu CPF")
Nc= str(input("Digite seu nome completo: "))
CPF = float(input("CPF: "))
data = int(input("digite a sua data de nascimento: "))

print(40*"---")
print("SETOR DE PAGAMENTO:")

#nessa area seria implantada api TransUnion para  a realização de uma consulta de credito
#exemplo de como seria:

score = 7
if score <=6:
    print("aluguel negado devido ao baixo poder de credito ")

else:
    print("é possivel realizar o aluguel")

#caso o cliente não queira a utilizar a consulta de credito, não sera necessario implantar uma API no programa!
