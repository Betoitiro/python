list1 = [
    [1,2,3,2,58],
    [8,9,6,3,6],
    [8,36,36,39,35],
    [58,2,3,6,5],
    [47,58,69,32,25]
]


for z in list1:
    print(z)

print()

for lista in list1:
    for item in lista:
        if (item %2) ==0:
            print("esse intem é par {}".format(item))
        elif item ==5:
            print("esse numero é 5 {}".format(item))
        elif (item %2) != 0:
            print("este numero é impar {} ".format(item))