def incializar_lista():
    for i in range(vertice):
        grafo.append([])

def adicionar_aresta(vertice_1, vertice_2):
    grafo[vertice_1-1].append(vertice_2)
    if vertice_1 != vertice_2:
        grafo[vertice_2-1].append(vertice_1)

def mostrar_lista():
    for i in range(vertice):
        print(f'{i+1}: {grafo[i]}')

grafo = []
vertice = int (input('Numero de vertices: '))
incializar_lista()
adicionar_aresta(1, 2)
adicionar_aresta(1, 3)
adicionar_aresta(2, 3)
mostrar_lista()