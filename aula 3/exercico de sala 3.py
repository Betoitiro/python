num = int(input("Digite um numero inteiro: "))

if num >1:
    for i in range(2, num):
        if (num % i) ==0:
            print(num, "o numero não é primo")
            break

        else:
            print(num, "o numero é primo")