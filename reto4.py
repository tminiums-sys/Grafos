def recorrido_amplitud(grafo, inicio):
    if inicio not in grafo:
        return []
    
    visitados = []
    cola = [inicio]
    
    while cola:
        actual = cola.pop(0)
        if actual not in visitados:
            visitados.append(actual)
            for vecino in grafo[actual]:
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)
    
    return visitados
