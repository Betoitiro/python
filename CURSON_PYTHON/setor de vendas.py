import time
print("===== Cravo e Canela =====")
time.sleep(1.5)
valor = float(input('Digite o valor do produto: '))

print('OPÇÕES DE PAGAMENTO:')
print('OPÇÃO [1] -> PAGAMENTO A VISTA, SUJEITO A 10% DE DESCONTO')
print('OPÇÃO [2] -> PAGAMENTO A VISTA NO CARTÃO, SUJEITO A 5% DE DESCONTO')
print('OPÇÃO [3] -> PARCELAMENTO EM ATE 2 VEZES, PAGAMENTO COM VALOR NORMAL')
print('OPÇÃO [4] -> PARCELAMENTO EM ATE 3 VEZES OU MAIS, COM TAXA DE 20% DE JUROS')

op = int(input('Escolha a forma de pagamento'))
if op == 1:
    desconto = valor - (valor*10/100)
    print("o produto desejado custava R${:.2f} com a forma de pagamento escolhida ficara por R${}." .format(valor,desconto))

elif op ==2:
    d2 = valor - (valor * 5 /100)
    print("o produto desejado custava R${:.2f} com a forma de pagamento escolhida ficara por R${}.".format(valor,d2))

elif op ==3:
    d3 = valor + (valor *20 / 100)
    print("o produto desejado custava R${:.2f} com a forma de pagamento escolhida ficara por R${}.".format(valor,d3))
else:
    print('opção não encontrada!')