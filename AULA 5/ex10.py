import heapq


def dik(grafo, origem, destino):
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0

    vertices_nao_visitados = [(0, origem)]
    vertices_visitados = set()

    vertices_pai = {}

    while vertices_nao_visitados:
        (dist, vertice_atual) = heapq.heappop(vertices_nao_visitados)

        if vertice_atual == destino:
            caminho = []
            while vertice_atual in vertices_pai:
                caminho.append(vertice_atual)
                vertice_atual = vertices_pai[vertice_atual]
            caminho.append(origem)
            caminho.reverse()
            return caminho

        vertices_visitados.add(vertice_atual)

        for adjacente, peso in grafo[vertice_atual].items():
            if adjacente not in vertices_visitados:
                nova_distancia = dist + peso
                if nova_distancia < distancias[adjacente]:
                    distancias[adjacente] = nova_distancia
                    vertices_pai[adjacente] = vertice_atual
                    heapq.heappush(vertices_nao_visitados, (nova_distancia, adjacente))

    return None


grafo = {'A': {'X':5, 'C':10}, 'X': {'D':3}, 'C':{'D:7'}, 'D':{}}
orig = 'A'
dest = 'D'
rota = dik(grafo,orig, dest)
print(rota)