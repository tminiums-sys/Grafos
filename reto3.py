def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

def agregar_arista(grafo, origen, destino):
    # No permitir lazos
    if origen == destino:
        return
    
    # No agregar si alguno no existe
    if origen not in grafo or destino not in grafo:
        return
    
    # Evitar duplicados
    if destino not in grafo[origen]:
        grafo[origen].append(destino)
    if origen not in grafo[destino]:
        grafo[destino].append(origen)
