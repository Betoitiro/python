number=[]
for i in range(20):
    number.append(int(input("digite o {i + 1} numero")))

    numeros_iv = number[::-1]

    print("ordem invertida: ")
    for num in numeros_iv:
        print(num)
