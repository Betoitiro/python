m1 = float(input("Digite a primeira nota: "))
m2 = float(input("Digite a segunda nota: "))
media = (m1 + m2)/2
if media >=7:
    print("o aluo esta aprovado com a media de {}".format(media))
elif media <7:
    print("o aluno esta reporvado com a media {}".format(media))
else:
    print("dado não encontrado")