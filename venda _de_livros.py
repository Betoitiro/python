print(25*"tabela de lvros")
print("classe A", end="\n")
print("\n")

#banco de dados do sistema, cada livro novo ou alteração devera ser feita aqui
amoreazeitonas = "amor e azeitonas"
diariodeumbanana = "diario de um banana"
herrypottereacamarasecreta = "herry potter e a camera secreta"

print(amoreazeitonas)
print(diariodeumbanana)
print(herrypottereacamarasecreta)

print(40*("---"))

#caso tenha mais opções, devera ser adicionada na lista abaixo e colocada a alterativa no sistema
opcoes = [ "1. deseja comprar 1 livro", "2. deseja comprar 2 livros", "3. deseja comprar 3 livros"]

#loop for para o sistema de repetição
for opc in opcoes:
    print(opc)

#aonde o cliente efetuara a escolha de quantos livros deseja comprar
escolha = int(input("escolha quantos livros vc deseja comprar: "))

print(40*("---"))


#caso seja selecionado a opção 1, o sistema encaminhara para essas condiocções abaixo
if escolha == 1:
    print("voce escolheu a opção 1")
    
    sc = str(input("escolha o lvro desejado: ")).lower() 
    #foi inserido um lower para deixar todas as letras minusculas, assim evitando erros do sistema
    
    esc = sc.replace(" ", "")
    #o replace tambem foi implantado para evitar erros, assim toda frase digitada ficara sem espaços evitando falhas

    #com esses comandos acima todos os caracteres inseridos ficarão minusculos e sem espaço


    if esc == "herrypottereacamarasecreta":
        #todos os nomes dos livros devem ser escritos sem espaços e todo em minusculas devido aos comandos de cima
        print("esse livro custa R$ 100,00 ")
    
    elif esc =="diariodeumbanana":
        print("esse livro custa R$120")
    
    elif esc == "amoreazeitonas":
        print("esse livr custa R$150.00")

    else:
        print("nenhuma opção escolhida")


elif escolha == 2:
    sc2 = str(input("escolha o primeiro livro: ")).lower()
    sc3 = str(input("escolha o segundo livro: ")).lower()
    #o comando lower se repete nas mesmas, pelos os mesmos obejtivos

    esc2 = sc2.replace(" ","")
    esc3 = sc3.replace(" ","")    
    #o replace fez que tivesse que criar outra variavel, para que ela seja escrita sem espaço

    print(40*"---")

    if esc2 == "amoreazeitonas" and esc3 == "diariodeumbanana":
        print("os livros escolhidos foram: amor e azeitonas e diario de um banana. o valor total da compra sera de R$ 270.00")
    
    elif esc2== "diariodeumbanana" and esc3 == "amoreazeitonas":
         print("os livros escolhidos foram: amor e azeitonas e diario de um banana. o valor total da compra sera de R$ 270.00")

    elif esc2 == "amoreazeitonas" and esc3== "herrypottereacamarasecreta":
        print("os livros escolhidos foram: amor e azeitonas Herry potter e a camera secreta. O valor total da compra sera de R$ 220,00")

    elif esc2 == "herrypottereacamarasecreta" and esc3 == "amoreazeitonas":
        print("os livros escolhidos foram: amor e azeitonas Herry potter e a camera secreta. O valor total da compra sera de R$ 220,00")
     
    elif esc2 == "amoreazeitonas" and esc3== "amoreazeitonas":
        print("voce escolheu dois livros iguais. O valor total da compra foi de R$ 300,00")

    elif esc2 == "diariodeumbanana" and esc3 == "herrypottereacamarasecreta":
        print("os livros escolhidos foram: diario de um banana e herry potter e a camara secreta. O valor total da venda ficara no total de R$120,00")
    
    elif esc2 == "herrypottereacamarasecreta" and esc3 == "diariodeumbanana":
        print("os livros escolhidos foram: diario de um banana e herry potter e a camara secreta. O valor total da venda ficara no total de R$120,00")

    elif esc2 == "diariodeumbanana" and esc3 =="diariodeumbanana":
        print("voce esclheu dois livros iguais. O valor total da compra foi de R$ 240,00")
    
    elif esc2 == "herrypottereacamarasecreta" and esc3 =="herrypottereacamarasecreta":
        print("voce esclheu dois livros iguais. O valor total da compra foi de R$ 200,00")

    else:
        print("pesquisa não escontrada!", "\n")
        print("tente novamente!")


elif escolha == 3:
    print("o sistema ta em manutenção, por gentileza, escolha a opção 1 e logo em seguida a opção 2!", "\n")
    print("Obrigado pela compreenção!")

#caso queira acrecentar mais uma opção de escolha, é so seguir o mesmo esquema acima
# elif escolha ==4:
    #....

else:
    print("nenhuma opção encontrada!", "\n")
    print("tente novamente!")
    #feixamento do sistema


    
    



'''
parte texte do sistema para a maniulação das string


esc1 = str(input("escolha o lvro desejado: ")).lower()
esc2 = str(input("digite qual o outro livro que deseja comprar:")).lower
sc = esc.replace(" ","")
sc2 = esc2.replace(" ","")
print(sc)
print(sc2)
'''
