nome = str(input("digite seu nome: "))
segundo_nome = str(input(("digite o seu segundo nome: ")))
idade = int(input("digite a sua idade: "))
cidade = str(input((" digite a sua cidade: ")))

amigo = {'nome' : nome,
         'segundo nome': segundo_nome,
         'idade': idade,
         'cidade' : cidade
}

print('o seu primeiro nome é {}, '
      'o seu segundo nome é {},'
      'tem {} anos de idade,'
      'e habita em {}'
      .format(amigo['nome'], amigo['segundo nome'], amigo['idade'], amigo['cidade']))