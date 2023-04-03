nome = str(input('Digite seu nome: '))
print('seja bem vindo senhor(a) {}!' .format(nome))
print(40*'--')
salario = float(input('Digite o valor do seu salario: '))
valc= float(input('Digite o valor da casa: '))
vale= float(input('valor da entrada: '))
rest = valc - vale
print('o valor da casa  era de {:.2f} com uma entrada de {:.2f} ficou por {:.2f}' .format(valc, vale,rest))
print(40*'--')
tempo = int(input('quanto messes sera o emprestimo? '))
valp = rest / tempo
print('cada parcela ficara por {}' .format(valp))
if valp > salario-(salario*30/100):
    print('emprestimo negado!')
else:
    print('emprestimo concedido!')

print(20*'--')
print('OBS: CASO O VALOR DO EMPRESTIMO ULTRAPASSE 30% DO VALOR DO SALARIO O EMPRESTIMO SERA SEGADO')
print(20*'!-!')
print('informações decorrente a compra: valor da casa foi {}, numero de parcelas  foi de {}, valor de cada parcela {}' .format(valc,tempo,valp))