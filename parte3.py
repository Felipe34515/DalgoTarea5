import sys 

def cargar_grafo()->list:
    linea = sys.stdin.readline()
    grafo = []
    while linea != "":
        lista = []
        for n in linea.split("\t"):
            lista.append(int(n))
        grafo.append(lista)
        linea = sys.stdin.readline()

    return grafo

def dfs(grafo: list, u: int)->bool:
    colores[u] = "GRIS"

    for v in grafo[u]:
        if colores[v] == "GRIS":
            return True

        if colores[v] == "BLANCO" and dfs(grafo, v):
            return True

    colores[u] = "NEGRO"
    return False


def es_ciclico():
    #Llamar al dfs iniciando desde 0 hasta todos los nodos o hasta que encuentre un ciclo
    for i in range(0, len(grafo)):
        if colores[i] == "BLANCO" and dfs(grafo, i):
            return True
    return False

grafo = cargar_grafo()
colores = []

# Hacer que todos los vertices iniciamente sean blancos
for __ in range(0, len(grafo)):
    colores.append("BLANCO")
print(es_ciclico())

