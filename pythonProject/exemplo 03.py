import json

lista = {
   'frutas' : {'abacate': 2.99, 'uva': 2.5, 'kiwi': 5.50},
    'data' : '2023-05-2023'
}

with open('arquivo.json',  'w') as arquivo:
    json.dump(lista, arquivo)
    meu_json = json.dumps(lista)