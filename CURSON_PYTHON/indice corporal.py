#calculando o IMC

peso = float(input('Qual é o seu peso? {kg)'))
alt = float(input('Qual é a sua altura? (m) '))
imc = peso/(alt**2)
print('o seu imc é {}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc <40:
    print('obesidade')
elif imc > 40:
    print('obsesidade morbida')