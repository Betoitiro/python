from random import randint
it = ('pedra', 'papel', 'tesoura')
comp= randint(0,2)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jo = int(input('Qual a sua jogada? '))
print(10*'===')
print('O computador jogou {}'.format(it[comp]))
print(' o jogador jogou {}'.format(it[jo]))
print(10*'===')

if comp == 0:
    if jo == 0:
        print('empate')
    elif jo == 1:
        print('Jogador vence')
    elif jo == 2:
        print('computador vence')
    else:
        print('jogada invalida')
elif comp ==1:
    if jo ==0:
        print('computador vence')
    elif jo == 1:
        print('empate')
    elif jo == 2:
        print('jogador vence')
    else:
        print('jogada invalida')


elif comp == 2:
    if jo ==0:
        print('jogador vence')
    elif jo == 1:
        print('Jogador vence')
    elif jo == 2:
        print('empate')
    else:
        print('jogada invalida')