import csv


with open('C:\Users\itiro\Documents\python\Aula 12\fill.csv', 'r', newline='', encoding='utf-8') as arquivo:
    filmes = csv.reader(arquivo, delimiter=',')
    print(filmes)

    _visualizaçã_oMAX = 2
    _filmes_maisVistos = ""

for linhas in filmes:
  #  print(_visualizaçã_oMAX)
    NomeFilmes = linhas[2]
    Visu = int(linhas[8])
    
    # if(Visu > _visualizaçã_oMAX):
    #     print(Visu)