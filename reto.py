def contar_vertices(grafo):
    return len(grafo)

def contar_aristas(grafo):
    total = 0
    for vertice in grafo:
        total += len(grafo[vertice])
    return total // 2
