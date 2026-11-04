def estan_conectados(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    return destino in grafo[origen]
