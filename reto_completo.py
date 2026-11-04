grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

def mostrar_vecinos(grafo, vertice):
    if vertice not in grafo:
        return []
    return grafo[vertice]

def contar_vertices(grafo):
    return len(grafo)

def contar_aristas(grafo):
    total = 0
    for vertice in grafo:
        total += len(grafo[vertice])
    return total // 2

def estan_conectados(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    return destino in grafo[origen]

def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

def agregar_arista(grafo, origen, destino):
    if origen == destino:
        return
    if origen not in grafo or destino not in grafo:
        return
    if destino not in grafo[origen]:
        grafo[origen].append(destino)
    if origen not in grafo[destino]:
        grafo[destino].append(origen)

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

# Pruebas
print(mostrar_vecinos(grafo, "C"))
print(contar_vertices(grafo))
print(contar_aristas(grafo))
print(estan_conectados(grafo, "A", "B"))
print(estan_conectados(grafo, "A", "F"))
print(estan_conectados(grafo, "X", "A"))
agregar_vertice(grafo, "G")
agregar_arista(grafo, "F", "G")
print(grafo["F"])
print(grafo["G"])
print(recorrido_amplitud(grafo, "A"))
print(existe_ruta(grafo, "A", "F"))
print(existe_ruta(grafo, "A", "A"))
print(existe_ruta(grafo, "A", "X"))
