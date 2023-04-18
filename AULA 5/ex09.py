import math

def distancia_entre_pontos(px, py):
    return math.sqrt((px[0] - py[0])**2 + (px[1] - py[1]) ** 2 + (px[2] - py[2]) **2 + (px[3] - py[3])**2)

def d_total(pontos):
    dis_total = 0
    for i in range(len(pontos) - 1):
        dis_total += distancia_entre_pontos(pontos[i], pontos[i+1])
    return dis_total

pontos = [( 5 ,6 , 8, 9), ( 11, 2 ,15, 16),(4,7,17,13)]
print("a distancia total ente os pontos é de aproximadamente {:.2f}".format(d_total(pontos)))