num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das base de conversão:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal
''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para binario é igual a {}'.format(num,bin(num)))
elif op == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif op == 3:
    print('{} convertido em hexadecimal é igual a {}'.format(num, hex(num)))