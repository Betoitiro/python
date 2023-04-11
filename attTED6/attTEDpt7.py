from collections import UserString


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

        USUARIO.append(user)

    else:
        print("acesso negado")

for user in UserString:
    print("nome: {}, idade: {}, email: {}".format(user["nome"], user["idade"], user["email"]))