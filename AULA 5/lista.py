#listas de nomes
lists = ["humberto", "uchoa", "jp", "remerson", "paulo"]
print(lists)
print(len(lists)) #ver o tamanho da lista
print(type(lists))
print(lists[0])
print(lists[1])
print(lists[2])
print(lists[3])
print(lists[4])


#listas de frutas
print()
print()

frutas = ["pera", "uva", "maça", "kiwi"]
print(frutas[1])
frutas[1] = "abacaxi" #como alterar a variavel na lista
print(frutas[1])

frutas.insert(2, "abacate")
print(frutas)

#codigo para remover
del frutas[3]
print(frutas)

#codigo para adicionar uma variavel a lista
frutas.insert(3,"melão")
frutas.insert(5, "jaca")
print(frutas)

#codigo para deletar uma variavel pelo nome
del frutas[frutas.index("jaca")]
print(frutas)

pop_fruta = frutas.pop(frutas.index("ameixa"))
print('pop frutas {}'.format(pop_fruta))