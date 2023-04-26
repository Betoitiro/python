ano = int(input("Digite seu ano de nascimento: "))
idade = 2023 - ano
if idade >= 18 and idade <= 25:
    print("Sua idade ja é compativel para o alistamento militar")
elif idade >= 25 and idade <=42:
    print('Voce deve se alistar imediatemente!!')
elif idade <18:
    print('sua idade ainda não é compativel para o alistamento miliar')
else:
    print('Sua idade ja esta alem do permitdo para o alistamento')
print(idade)