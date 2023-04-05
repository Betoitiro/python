u = []

while True:
    op = str(input("Deseja iniciar um novo usuario? (y/n)"))

    if op =="n":
        break
    elif op == "s":
        nome = input("digite o nome de usuario que voce deseja: ")
        id = input("digite a sua idade: ")
        em = input("digite o seu email")

        user = {"nome": nome, "idade" :id, "email" : em}

        users.append(user)

    else:
        print("acesso negado")

for user in users:
    print("nome: {}, idade {}, email {}". format(nome, id,em))