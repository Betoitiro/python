n1 = float(input("digite uma nota: "))
n2 = float(input("digite a segunda nota: "))
m = (n1 + n2)/2
if m < 6:
    print("a primeira nota foi {}, e a segunda nota foi {}, logo a media foi {},logo o aluno foi reprovado".format(n1,n2,m))

elif m>=6:
    print("a primeira nota foi {}, e a segunda nota foi {}, logo o aluno aprovado".format(n1,n2))