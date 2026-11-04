def existe_ruta(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    
    visitados = []
    cola = [origen]
    
    while cola:
        actual = cola.pop(0)
        
        if actual == destino:
            return True
        
        if actual not in visitados:
            visitados.append(actual)
            for vecino in grafo[actual]:
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)
    
    return False
