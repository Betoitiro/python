aluno1 = {'nome' : 'remerson', 'idade' : 24}
aluno2 = { 'nome' : 'humberto', 'idade': 17}
aluno3 = {'nome ': 'paulo', 'idade': 25}
print(aluno1['nome'])


print('o aluno {}, tem {} anos de idade'.format(aluno1['nome'], aluno1['idade']))

aluno2['email'] = 'itirohumberto@gmail.com'
print("o aluno {}, tem {} anos de idade e  seu email é {}". format(aluno2['nome'], aluno2['idade'], aluno2['email']))