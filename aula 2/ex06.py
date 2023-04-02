estoque = float(input("digite o estoque atual:"))
cpmx = float(input("digite a capacidade maxima do estoque: "))
cpmin = float(input("digite a capacidade minima do estoque: "))
media = (cpmx + cpmin)/2
print("a media foi de: {}".format(media))
if media >= estoque:
    print("não efetuar compra!")
else:
    print("efetuar compra!")