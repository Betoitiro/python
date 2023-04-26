#classificando de acordo com a idade
# ate 9 anos : mirim
# ate 14 anos : infantil
# ate 19 anos : junior
# ate 25 ano: senior
#acima dos 25: Master

from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento: '))
idade = atual - nas
print("O atleta tem {} anos de idade".format(idade))
if idade <=9:
    print('classificação mirim')
elif idade <=14:
    print('classificação infantil')
elif idade <=19:
    print('classificação junior')
elif idade <=25:
    print("classificação senior")
elif idade > 25:
    print('classificação master')
