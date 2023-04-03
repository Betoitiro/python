#digite um numero de 1 a 100, e empremima uma mensagem se o numero for mutiplo de 3 ou 5
#se for mutiplo de 3 digite tree, caso seja de 5 imprima pent
#sor for mutiplo dos dois imprima redtree

for num in range(1, 101):
    if num %3 == 0 and num % 5 ==0 : #vai veriicar se a divisão de receber o resto 0, o numero é multiplo dos dois
        print("redtree")
    elif num % 3 == 0: #se o resto da divisão for 0, o numero desse caso sera multiplo de 3
        print("tree")
    elif num % 5 ==0: #se o resto da divisão dor 0, o numero sera multiplo de 5
        print("pent")
    else: 
        print(num)